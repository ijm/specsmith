#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script for the TECHDOC encoding converter.
"""

import sys
import tempfile
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

import convertEncoding
from encodingMD import parse as md_parse, serialize as md_serialize
from encodingJSON import parse as json_parse, serialize as json_serialize
from encodingXML import parse as xml_parse, serialize as xml_serialize
from ast_nodes import Section, SectionType, Statement, Techdoc, VerificationIndicator


def create_test_techdoc() -> Techdoc:
    """Create a test TECHDOC AST."""
    sections = [
        Section(
            name="Summary",
            section_type=SectionType.NARRATIVE,
            statements=[
                Statement(content="This is a test TECHDOC document."),
                Statement(content="It demonstrates the encoding conversion functionality."),
            ],
        ),
        Section(
            name="Constraints",
            section_type=SectionType.ASSERTION,
            statements=[
                Statement(
                    content="All scripts MUST use proper error handling.",
                    statement_id="T01",
                    verification_indicator=VerificationIndicator.PROVABLE,
                ),
                Statement(
                    content="Code SHOULD be well-documented.",
                    statement_id="T02",
                    verification_indicator=VerificationIndicator.HEURISTIC,
                ),
            ],
        ),
        Section(
            name="Configuration",
            section_type=SectionType.DATA,
            statements=[],
            data_language="json",
            data_content='{"debug": true, "version": "1.0.0"}',
        ),
    ]
    
    return Techdoc(title="Test Document", sections=sections)


def test_markdown_roundtrip():
    """Test Markdown parsing and serialization."""
    print("Testing Markdown roundtrip...")
    
    # Create test document
    original_ast = create_test_techdoc()
    
    # Serialize to Markdown
    md_content = md_serialize(original_ast)
    print("Markdown output:")
    print(md_content)
    print("-" * 50)
    
    # Parse back to AST
    parsed_ast = md_parse(md_content)
    
    # Verify structure
    assert parsed_ast.title == original_ast.title
    assert len(parsed_ast.sections) == len(original_ast.sections)
    
    for orig_section, parsed_section in zip(original_ast.sections, parsed_ast.sections):
        assert orig_section.name == parsed_section.name
        assert orig_section.section_type == parsed_section.section_type
        assert len(orig_section.statements) == len(parsed_section.statements)
    
    print("✓ Markdown roundtrip test passed")


def test_json_roundtrip():
    """Test JSON parsing and serialization."""
    print("Testing JSON roundtrip...")
    
    # Create test document
    original_ast = create_test_techdoc()
    
    # Serialize to JSON
    json_content = json_serialize(original_ast)
    print("JSON output:")
    print(json_content)
    print("-" * 50)
    
    # Parse back to AST
    parsed_ast = json_parse(json_content)
    
    # Verify structure
    assert parsed_ast.title == original_ast.title
    assert len(parsed_ast.sections) == len(original_ast.sections)
    
    for orig_section, parsed_section in zip(original_ast.sections, parsed_ast.sections):
        assert orig_section.name == parsed_section.name
        assert orig_section.section_type == parsed_section.section_type
        assert len(orig_section.statements) == len(parsed_section.statements)
    
    print("✓ JSON roundtrip test passed")


def test_xml_roundtrip():
    """Test XML parsing and serialization."""
    print("Testing XML roundtrip...")
    
    # Create test document
    original_ast = create_test_techdoc()
    
    # Serialize to XML
    xml_content = xml_serialize(original_ast)
    print("XML output:")
    print(xml_content)
    print("-" * 50)
    
    # Parse back to AST
    parsed_ast = xml_parse(xml_content)
    
    # Verify structure
    assert parsed_ast.title == original_ast.title
    assert len(parsed_ast.sections) == len(original_ast.sections)
    
    for orig_section, parsed_section in zip(original_ast.sections, parsed_ast.sections):
        assert orig_section.name == parsed_section.name
        assert orig_section.section_type == parsed_section.section_type
        assert len(orig_section.statements) == len(parsed_section.statements)
    
    print("✓ XML roundtrip test passed")


def test_cli_conversion():
    """Test CLI conversion functionality."""
    print("Testing CLI conversion...")
    
    # Create test document
    original_ast = create_test_techdoc()
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Test MD -> JSON
        md_file = temp_path / "test.md"
        json_file = temp_path / "test.json"
        xml_file = temp_path / "test.xml"
        
        # Write original MD
        md_content = md_serialize(original_ast)
        md_file.write_text(md_content)
        
        # Convert MD to JSON
        convertEncoding.convert_document(
            from_module="encodingMD",
            to_module="encodingJSON",
            input_path=str(md_file),
            output_path=str(json_file),
        )
        
        # Convert JSON to XML
        convertEncoding.convert_document(
            from_module="encodingJSON",
            to_module="encodingXML",
            input_path=str(json_file),
            output_path=str(xml_file),
        )
        
        # Convert XML back to MD
        final_md_file = temp_path / "final.md"
        convertEncoding.convert_document(
            from_module="encodingXML",
            to_module="encodingMD",
            input_path=str(xml_file),
            output_path=str(final_md_file),
        )
        
        # Verify final content
        final_content = final_md_file.read_text()
        final_ast = md_parse(final_content)
        
        assert final_ast.title == original_ast.title
        assert len(final_ast.sections) == len(original_ast.sections)
    
    print("✓ CLI conversion test passed")


def main():
    """Run all tests."""
    print("Running TECHDOC converter tests...")
    print("=" * 50)
    
    try:
        test_markdown_roundtrip()
        test_json_roundtrip()
        test_xml_roundtrip()
        test_cli_conversion()
        
        print("=" * 50)
        print("All tests passed! ✓")
        
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
