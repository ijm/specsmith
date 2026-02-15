#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Markdown encoding module for TECHDOC documents.

This module provides functions to parse TECHDOC documents from Markdown format
and serialize TECHDOC AST objects to Markdown format, following the
techdoc-encoding-md.spec specification.
"""

import re
from typing import List

from ast_nodes import (
    Section,
    SectionType,
    Statement,
    Techdoc,
    VerificationIndicator,
)


class EncodingMDError(Exception):
    """Exception raised for Markdown encoding errors."""



def parse(content: str) -> Techdoc:
    """
    Parse a Markdown-encoded TECHDOC document into an AST.
    
    Args:
        content: Markdown string containing the TECHDOC document
        
    Returns:
        Techdoc AST object
        
    Raises:
        EncodingMDError: If Markdown parsing or validation fails
    """
    lines = content.splitlines()
    
    # Extract title (first level 2 heading)
    title = None
    current_line = 0
    
    # Skip comments and find title
    while current_line < len(lines):
        line = lines[current_line].strip()
        
        # Skip markdownlint comments
        if line.startswith("<!--"):
            current_line += 1
            continue
            
        if line.startswith("## "):
            title = line[3:].strip()
            current_line += 1
            break
        
        current_line += 1
    
    if title is None:
        raise EncodingMDError("No level 2 heading found for document title")
    
    sections: List[Section] = []
    
    # Parse sections
    while current_line < len(lines):
        # Skip empty lines
        while current_line < len(lines) and not lines[current_line].strip():
            current_line += 1
        
        if current_line >= len(lines):
            break
        
        # Extract section name
        line = lines[current_line].strip()
        if not line.startswith("### "):
            raise EncodingMDError(f"Expected section heading at line {current_line + 1}, found: {line}")
        
        section_name = line[4:].strip()
        current_line += 1
        
        # Parse section content
        section, current_line = _parse_section(section_name, lines, current_line)
        sections.append(section)
    
    return Techdoc(title=title, sections=sections)


def _parse_section(section_name: str, lines: List[str], start_line: int) -> tuple[Section, int]:
    """Parse a section starting from given line."""
    current_line = start_line
    
    # Collect section content until next heading
    section_lines = []
    while current_line < len(lines):
        line = lines[current_line].strip()
        
        # Stop at next section heading
        if line.startswith("### "):
            break
        
        # Skip comments
        if line.startswith("<!--"):
            current_line += 1
            continue
            
        section_lines.append(lines[current_line])
        current_line += 1
    
    # Remove leading empty lines
    while section_lines and not section_lines[0].strip():
        section_lines.pop(0)
    
    # Check for special section types
    section_lower = section_name.lower()
    if "inheritance" in section_lower:
        # Parse as inheritance section
        return _parse_inheritance_section(section_name, section_lines), current_line
    elif section_lines and section_lines[0].strip().startswith("```"):
        # Data section
        return _parse_data_section(section_name, section_lines), current_line
    elif any(line.strip().startswith(("* ", "- ")) for line in section_lines):
        # Assertion section (has list items)
        return _parse_assertion_section(section_name, section_lines), current_line
    else:
        # Narrative section
        return _parse_narrative_section(section_name, section_lines), current_line


def _parse_inheritance_section(section_name: str, section_lines: List[str]) -> Section:
    """Parse an inheritance section with structured subsections."""
    conforms_to: List[str] = []
    inherits: List[str] = []
    current_subsection = None
    
    for line in section_lines:
        line_stripped = line.strip()
        
        if not line_stripped:
            continue
        
        # Check for subsection headers (level 4)
        if line_stripped.startswith("#### "):
            subsection_name = line_stripped[5:].strip().lower()
            current_subsection = subsection_name
            continue
        
        # Check for list items (immediately after subsection header or with blank line)
        if line_stripped.startswith("* ") or line_stripped.startswith("- "):
            content = line_stripped[2:].strip()
            
            if current_subsection == "conforms to" or current_subsection == "conformance":
                conforms_to.append(content)
            elif current_subsection == "inherits" or current_subsection == "inheritance":
                inherits.append(content)
    
    return Section(
        name=section_name,
        section_type=SectionType.INHERITANCE,
        statements=[],  # Inheritance sections use structured data instead
        conforms_to=conforms_to if conforms_to else None,
        inherits=inherits if inherits else None,
    )


def _parse_data_section(section_name: str, section_lines: List[str]) -> Section:
    """Parse a data section from fenced code block."""
    if not section_lines or not section_lines[0].strip().startswith("```"):
        raise EncodingMDError(f"Data section '{section_name}' missing fenced code block")
    
    # Extract language and content
    first_line = section_lines[0].strip()
    language = first_line[3:].strip()  # Remove "```"
    
    # Find closing fence
    content_lines = []
    for line in section_lines[1:]:
        if line.strip().startswith("```"):
            break
        content_lines.append(line)
    
    content = "\n".join(content_lines).strip()
    
    return Section(
        name=section_name,
        section_type=SectionType.DATA,
        statements=[],
        data_language=language,
        data_content=content,
    )


def _parse_assertion_section(section_name: str, section_lines: List[str]) -> Section:
    """Parse an assertion section from markdown list."""
    statements: List[Statement] = []
    
    for line in section_lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
        
        # Check if it's a list item
        if line_stripped.startswith("* ") or line_stripped.startswith("- "):
            # Remove list marker
            content = line_stripped[2:].strip()
            
            # Parse statement with optional ID and verification indicator
            statement = _parse_list_item(content)
            statements.append(statement)
        # Handle multi-line statements (continuation lines)
        elif statements and not line_stripped.startswith(("* ", "- ")):
            # This is a continuation of the previous statement
            if statements:
                statements[-1].content += " " + line_stripped
    
    # Determine section type based on content
    section_type = _determine_section_type(section_name, statements)
    
    return Section(
        name=section_name,
        section_type=section_type,
        statements=statements,
    )


def _parse_list_item(content: str) -> Statement:
    """Parse a list item statement."""
    # Match pattern: "ID content [verification_indicator]"
    match = re.match(r"^([A-Z]\d+)\s+(.*?)(?:\s+([ⓅⓉⒺⒽⓃ]))?\s*$", content)
    
    if match:
        statement_id = match.group(1)
        statement_content = match.group(2).strip()
        verification_char = match.group(3)
        
        # Check for normative indicators in content if no explicit verification indicator
        if verification_char is None:
            normative_indicators = ["MUST", "MUST NOT", "SHOULD", "SHOULD NOT", "MAY", "NOT"]
            content_upper = statement_content.upper()
            
            for indicator in normative_indicators:
                if indicator in content_upper:
                    # This is a normative statement - assign default verification
                    verification_indicator = VerificationIndicator.HEURISTIC  # Default for normative statements
                    break
            else:
                verification_indicator = None
        else:
            verification_indicator = VerificationIndicator.from_unicode(verification_char)
            if verification_indicator is None:
                raise EncodingMDError(f"Invalid verification indicator: {verification_char}")
        
        return Statement(
            content=statement_content,
            statement_id=statement_id,
            verification_indicator=verification_indicator,
        )
    else:
        # No ID, treat as narrative statement
        return Statement(content=content)


def _determine_section_type(section_name: str, statements: List[Statement]) -> SectionType:
    """Determine section type based on section name and statement content."""
    # Definition sections typically contain indicative statements (no verification indicators)
    definition_keywords = ["definition", "terminology", "vocabulary", "conventions", "inheritance"]
    
    # Check if section name suggests it's a definition or inheritance section
    section_lower = section_name.lower()
    if any(keyword in section_lower for keyword in definition_keywords):
        return SectionType.ASSERTION  # But with indicative statements
    
    # Check if any statements have verification indicators (normative)
    has_normative = any(stmt.verification_indicator is not None for stmt in statements)
    
    if has_normative:
        return SectionType.ASSERTION
    elif any(stmt.statement_id is not None for stmt in statements):
        # Has IDs but no verification indicators - indicative assertions
        return SectionType.ASSERTION
    else:
        return SectionType.NARRATIVE


def _parse_narrative_section(section_name: str, section_lines: List[str]) -> Section:
    """Parse a narrative section from freeform markdown."""
    # Join all content and preserve structure
    content = "\n".join(section_lines).strip()
    
    if not content:
        statements = []
    else:
        # For narrative sections, we need to preserve the original structure
        # Check if this looks like it should be an assertion section (has list items with IDs)
        has_list_items = any(line.strip().startswith(("* ", "- ")) for line in section_lines)
        has_ids = False
        
        if has_list_items:
            for line in section_lines:
                line_stripped = line.strip()
                if line_stripped.startswith(("* ", "- ")):
                    list_content = line_stripped[2:].strip()
                    if re.match(r"^[A-Z]\d+", list_content):
                        has_ids = True
                        break
        
        # If it has list items with IDs, it should be an assertion section
        if has_ids:
            return _parse_assertion_section(section_name, section_lines)
        
        # Otherwise, treat as narrative - preserve the original content as single statement
        statements = [Statement(content=content)]
    
    return Section(
        name=section_name,
        section_type=SectionType.NARRATIVE,
        statements=statements,
    )


def serialize(ast: Techdoc) -> str:
    """
    Serialize a TECHDOC AST to Markdown format.
    
    Args:
        ast: Techdoc AST object
        
    Returns:
        Markdown string representation
        
    Raises:
        EncodingMDError: If serialization fails
    """
    lines: List[str] = []
   
    # Always include markdownlint comment at the top (no blank line after)
    lines.append("<!-- markdownlint-disable MD041 -->")
   
    # Add title
    lines.append(f"## {ast.title}")
    lines.append("")

    # Add sections
    for i, section in enumerate(ast.sections):
        lines.append(f"### {section.name}")

        if section.section_type == SectionType.DATA:
            # Data section
            lines.append("")
            lines.append(f"```{section.data_language}")
            lines.append(section.data_content)
            lines.append("```")
        elif section.section_type == SectionType.INHERITANCE:
            # Inheritance section
            lines.append("")
            if section.conforms_to:
                lines.append("#### Conforms to")
                for item in section.conforms_to:
                    lines.append(f"* {item}")
                lines.append("")

            if section.inherits:
                lines.append("#### Inherits")
                for item in section.inherits:
                    lines.append(f"* {item}")
                lines.append("")
        else:
            # Narrative or assertion section
            lines.append("")
            for statement in section.statements:
                _serialize_statement(lines, statement)

        # Only add blank line between sections, not after the last one
        if i < len(ast.sections) - 1:
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _serialize_statement(lines: List[str], statement: Statement) -> None:
    """Serialize a statement to markdown."""
    if statement.verification_indicator is not None:
        # Normative statement
        verification_char = statement.verification_indicator.to_unicode()
        lines.append(f"* {statement.statement_id} {statement.content} {verification_char}")
        lines.append("")
    elif statement.statement_id is not None:
        # Indicative statement (definition) - always use list format
        lines.append(f"* {statement.statement_id} {statement.content}")
        lines.append("")
    else:
        # Pure narrative statement
        lines.append(statement.content)
        lines.append("")
