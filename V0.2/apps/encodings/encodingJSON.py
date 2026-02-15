#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
JSON encoding module for TECHDOC documents.

This module provides functions to parse TECHDOC documents from JSON format
and serialize TECHDOC AST objects to JSON format, following the
techdoc-encoding-json.spec specification.
"""

import json
from typing import Any, Dict, List, Union

from ast_nodes import (
    Section,
    SectionType,
    Statement,
    Techdoc,
    VerificationIndicator,
)


class EncodingJSONError(Exception):
    """Exception raised for JSON encoding errors."""


def parse(content: str) -> Techdoc:
    """
    Parse a JSON-encoded TECHDOC document into an AST.
    
    Args:
        content: JSON string containing the TECHDOC document
        
    Returns:
        Techdoc AST object
        
    Raises:
        EncodingJSONError: If JSON parsing or validation fails
    """
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise EncodingJSONError(f"Invalid JSON: {e}") from e
    
    # Validate top-level structure
    if not isinstance(data, dict):
        raise EncodingJSONError("Root must be a JSON object")
    
    if "title" not in data or "sections" not in data:
        raise EncodingJSONError("Missing required 'title' or 'sections' fields")
    
    if not isinstance(data["title"], str) or not isinstance(data["sections"], list):
        raise EncodingJSONError("'title' must be string and 'sections' must be array")
    
    # Parse sections
    sections: List[Section] = []
    for section_data in data["sections"]:
        section = _parse_section(section_data)
        sections.append(section)
    
    return Techdoc(title=data["title"], sections=sections)


def _parse_section(section_data: Dict[str, Any]) -> Section:
    """Parse a section from JSON data."""
    if not isinstance(section_data, dict):
        raise EncodingJSONError("Section must be a JSON object")
    
    if "name" not in section_data:
        raise EncodingJSONError("Section missing required 'name' field")
    
    name = section_data["name"]
    if not isinstance(name, str):
        raise EncodingJSONError("Section name must be a string")
    
    # Check for inheritance section
    if "conforms_to" in section_data or "inherits" in section_data:
        # Inheritance section
        conforms_to = section_data.get("conforms_to", [])
        inherits = section_data.get("inherits", [])
        
        if not isinstance(conforms_to, list) or not isinstance(inherits, list):
            raise EncodingJSONError("Inheritance section fields must be arrays")
        
        return Section(
            name=name,
            section_type=SectionType.INHERITANCE,
            statements=[],
            conforms_to=conforms_to,
            inherits=inherits,
        )
    
    elif "language" in section_data and "data" in section_data:
        # Data section
        data_language = section_data["language"]
        data_content = section_data["data"]
        
        if not isinstance(data_language, str) or not isinstance(data_content, str):
            raise EncodingJSONError("Data section 'language' and 'data' must be strings")
        
        return Section(
            name=name,
            section_type=SectionType.DATA,
            statements=[],
            data_language=data_language,
            data_content=data_content,
        )
    
    elif "content" in section_data:
        # Narrative or assertion section
        content = section_data["content"]
        if not isinstance(content, list):
            raise EncodingJSONError("Section 'content' must be an array")
        
        statements: List[Statement] = []
        for statement_data in content:
            statement = _parse_statement(statement_data)
            statements.append(statement)
        
        # Determine section type - check if it has any statements with IDs
        has_ids = any(stmt.statement_id is not None for stmt in statements)
        has_normative = any(
            stmt.verification_indicator is not None for stmt in statements
        )
        
        if has_normative:
            section_type = SectionType.ASSERTION
        elif has_ids:
            # Has IDs but no verification indicators - indicative assertions
            section_type = SectionType.ASSERTION
        else:
            section_type = SectionType.NARRATIVE
        
        return Section(name=name, section_type=section_type, statements=statements)
    
    else:
        raise EncodingJSONError(f"Section '{name}' has invalid structure")


def _parse_statement(statement_data: Union[str, Dict[str, Any]]) -> Statement:
    """Parse a statement from JSON data."""
    if isinstance(statement_data, str):
        # Pure narrative statement
        return Statement(content=statement_data)
    
    if not isinstance(statement_data, dict):
        raise EncodingJSONError("Statement must be a string or JSON object")
    
    if "content" not in statement_data:
        raise EncodingJSONError("Statement missing required 'content' field")
    
    content = statement_data["content"]
    if not isinstance(content, str):
        raise EncodingJSONError("Statement 'content' must be a string")
    
    statement_id = statement_data.get("id")
    verification_char = statement_data.get("verification")
    verification_type = statement_data.get("type")  # Handle old format
    
    verification_indicator = None
    if verification_char is not None:
        if not isinstance(verification_char, str):
            raise EncodingJSONError("Statement 'verification' must be a string")
        
        verification_indicator = VerificationIndicator.from_unicode(verification_char)
        if verification_indicator is None:
            raise EncodingJSONError(f"Invalid verification indicator: {verification_char}")
    elif verification_type is not None:
        # Handle old format with "type" field
        if not isinstance(verification_type, str):
            raise EncodingJSONError("Statement 'type' must be a string")
        
        try:
            verification_indicator = VerificationIndicator(verification_type)
        except ValueError:
            raise EncodingJSONError(f"Invalid verification type: {verification_type}")
    
    return Statement(
        content=content,
        statement_id=statement_id,
        verification_indicator=verification_indicator,
    )


def serialize(ast: Techdoc) -> str:
    """
    Serialize a TECHDOC AST to JSON format.
    
    Args:
        ast: Techdoc AST object
        
    Returns:
        JSON string representation
        
    Raises:
        EncodingJSONError: If serialization fails
    """
    try:
        data = {
            "title": ast.title,
            "sections": [_serialize_section(section) for section in ast.sections],
        }
        return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        raise EncodingJSONError(f"Serialization failed: {e}") from e


def _serialize_section(section: Section) -> Dict[str, Any]:
    """Serialize a section to JSON data."""
    base_data = {"name": section.name}
    
    if section.section_type == SectionType.DATA:
        base_data["language"] = section.data_language
        base_data["data"] = section.data_content
        return base_data
    elif section.section_type == SectionType.INHERITANCE:
        # Inheritance section
        if section.conforms_to:
            base_data["conforms_to"] = section.conforms_to
        if section.inherits:
            base_data["inherits"] = section.inherits
        return base_data
    else:
        # Narrative or assertion section
        base_data["content"] = [_serialize_statement(stmt) for stmt in section.statements]
        return base_data


def _serialize_statement(statement: Statement) -> Union[str, Dict[str, Any]]:
    """Serialize a statement to JSON data."""
    if statement.verification_indicator is None:
        # Narrative or indicative statement
        if statement.statement_id is not None:
            # Indicative statement - preserve the ID
            return {
                "id": statement.statement_id,
                "content": statement.content
            }
        else:
            # Pure narrative statement
            return statement.content
    
    # Normative statement
    verification_char = statement.verification_indicator.to_unicode()
    return {
        "id": statement.statement_id,
        "content": statement.content,
        "type": statement.verification_indicator.value,  # Use enum value instead of unicode
    }
