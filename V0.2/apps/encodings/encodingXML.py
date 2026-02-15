#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XML encoding module for TECHDOC documents.

This module provides functions to parse TECHDOC documents from XML format
and serialize TECHDOC AST objects to XML format, following the
techdoc-encoding-xml.spec specification.
"""

import xml.etree.ElementTree as ET
from typing import List

from ast_nodes import (
    Section,
    SectionType,
    Statement,
    Techdoc,
    VerificationIndicator,
)


class EncodingXMLError(Exception):
    """Exception raised for XML encoding errors."""


def parse(content: str) -> Techdoc:
    """
    Parse an XML-encoded TECHDOC document into an AST.
    
    Args:
        content: XML string containing the TECHDOC document
        
    Returns:
        Techdoc AST object
        
    Raises:
        EncodingXMLError: If XML parsing or validation fails
    """
    try:
        root = ET.fromstring(content)
    except ET.ParseError as e:
        raise EncodingXMLError(f"Invalid XML: {e}") from e
    
    # Validate root element
    if root.tag != "techdoc":
        raise EncodingXMLError(f"Root element must be 'techdoc', found '{root.tag}'")
    
    # Parse title
    title_elem = root.find("title")
    if title_elem is None or title_elem.text is None:
        raise EncodingXMLError("Missing required 'title' element")
    
    title = title_elem.text.strip()
    
    # Parse sections
    sections: List[Section] = []
    for section_elem in root.findall("section"):
        section = _parse_section(section_elem)
        sections.append(section)
    
    return Techdoc(title=title, sections=sections)


def _parse_section(section_elem: ET.Element) -> Section:
    """Parse a section from XML element."""
    name_attr = section_elem.get("name")
    if name_attr is None:
        raise EncodingXMLError("Section missing required 'name' attribute")
    
    name = name_attr.strip()
    
    # Check for inheritance section
    conforms_to_elem = section_elem.find("conforms_to")
    inherits_elem = section_elem.find("inherits")
    
    if conforms_to_elem is not None or inherits_elem is not None:
        # Inheritance section
        conforms_to = []
        inherits = []
        
        if conforms_to_elem is not None:
            for item_elem in conforms_to_elem.findall("item"):
                if item_elem.text is not None:
                    conforms_to.append(item_elem.text.strip())
        
        if inherits_elem is not None:
            for item_elem in inherits_elem.findall("item"):
                if item_elem.text is not None:
                    inherits.append(item_elem.text.strip())
        
        return Section(
            name=name,
            section_type=SectionType.INHERITANCE,
            statements=[],
            conforms_to=conforms_to if conforms_to else None,
            inherits=inherits if inherits else None,
        )
    
    # Check for data section
    data_elem = section_elem.find("data")
    if data_elem is not None:
        # Data section
        language_attr = data_elem.get("language")
        if language_attr is None:
            raise EncodingXMLError("Data section missing required 'language' attribute")
        
        if data_elem.text is None:
            raise EncodingXMLError("Data section missing content")
        
        return Section(
            name=name,
            section_type=SectionType.DATA,
            statements=[],
            data_language=language_attr.strip(),
            data_content=data_elem.text.strip(),
        )
    
    # Parse statements for narrative/assertion sections
    statements: List[Statement] = []
    for statement_elem in section_elem.findall("statement"):
        statement = _parse_statement(statement_elem)
        statements.append(statement)
    
    # Determine section type
    has_normative = any(
        stmt.verification_indicator is not None for stmt in statements
    )
    section_type = SectionType.ASSERTION if has_normative else SectionType.NARRATIVE
    
    return Section(name=name, section_type=section_type, statements=statements)


def _parse_statement(statement_elem: ET.Element) -> Statement:
    """Parse a statement from XML element."""
    if statement_elem.text is None:
        raise EncodingXMLError("Statement missing content")
    
    content = statement_elem.text.strip()
    
    # Check for normative statement attributes
    statement_id = statement_elem.get("id")
    type_attr = statement_elem.get("type")
    
    if statement_id is not None and type_attr is not None:
        # Normative statement
        try:
            verification_indicator = VerificationIndicator(type_attr.strip())
        except ValueError as exc:
            raise EncodingXMLError(f"Invalid verification indicator: {type_attr}") from exc
        
        return Statement(
            content=content,
            statement_id=statement_id.strip(),
            verification_indicator=verification_indicator,
        )
    
    else:
        # Narrative or indicative statement
        return Statement(content=content)


def serialize(ast: Techdoc) -> str:
    """
    Serialize a TECHDOC AST to XML format.
    
    Args:
        ast: Techdoc AST object
        
    Returns:
        XML string representation
        
    Raises:
        EncodingXMLError: If serialization fails
    """
    try:
        root = ET.Element("techdoc")
        
        # Add title
        title_elem = ET.SubElement(root, "title")
        title_elem.text = ast.title
        
        # Add sections
        for section in ast.sections:
            _serialize_section(root, section)
        
        # Generate XML string
        ET.indent(root, space="  ")
        return ET.tostring(root, encoding="unicode", xml_declaration=True)
    except Exception as e:
        raise EncodingXMLError(f"Serialization failed: {e}") from e


def _serialize_section(parent: ET.Element, section: Section) -> None:
    """Serialize a section to XML element."""
    section_elem = ET.SubElement(parent, "section")
    section_elem.set("name", section.name)
    
    if section.section_type == SectionType.DATA:
        # Data section
        data_elem = ET.SubElement(section_elem, "data")
        data_elem.set("language", section.data_language)
        data_elem.text = section.data_content
    elif section.section_type == SectionType.INHERITANCE:
        # Inheritance section
        if section.conforms_to:
            conforms_elem = ET.SubElement(section_elem, "conforms_to")
            for item in section.conforms_to:
                item_elem = ET.SubElement(conforms_elem, "item")
                item_elem.text = item
        
        if section.inherits:
            inherits_elem = ET.SubElement(section_elem, "inherits")
            for item in section.inherits:
                item_elem = ET.SubElement(inherits_elem, "item")
                item_elem.text = item
    else:
        # Narrative or assertion section
        for statement in section.statements:
            _serialize_statement(section_elem, statement)


def _serialize_statement(parent: ET.Element, statement: Statement) -> None:
    """Serialize a statement to XML element."""
    statement_elem = ET.SubElement(parent, "statement")
    statement_elem.text = statement.content
    
    if statement.verification_indicator is not None:
        statement_elem.set("id", statement.statement_id)
        statement_elem.set("type", statement.verification_indicator.value)
