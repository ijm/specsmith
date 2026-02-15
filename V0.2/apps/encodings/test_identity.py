#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Identity test script for TECHDOC encoding conversions.

This script tests that roundtrip conversions preserve all TECHDOC information
as required by techdoc-encoding.spec E03: conversion from ENCODING X 
to ENCODING Y and back to ENCODING X MUST preserve all TECHDOC information.
"""

import json
import sys
import tempfile
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

import convertEncoding
from encodingMD import parse as md_parse, serialize as md_serialize
from encodingJSON import parse as json_parse, serialize as json_serialize
from encodingXML import parse as xml_parse, serialize as xml_serialize
from ast_nodes import Techdoc


def normalize_xml(xml_content: str) -> str:
    """Normalize XML content for comparison by removing whitespace differences."""
    import xml.etree.ElementTree as ET
    
    try:
        root = ET.fromstring(xml_content)
        # Re-serialize with consistent formatting
        ET.indent(root, space="  ")
        return ET.tostring(root, encoding="unicode", xml_declaration=True)
    except ET.ParseError:
        return xml_content


def normalize_json(json_content: str) -> str:
    """Normalize JSON content for comparison."""
    try:
        data = json.loads(json_content)
        return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
    except json.JSONDecodeError:
        return json_content


def normalize_markdown(md_content: str) -> str:
    """Normalize Markdown content for comparison."""
    # Normalize line endings and trailing whitespace
    lines = [line.rstrip() for line in md_content.splitlines()]
    # Remove leading/trailing empty lines and normalize single trailing newline
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) + "\n"


def test_xml_identity() -> bool:
    """Test XML roundtrip identity (XML -> JSON -> XML)."""
    print("Testing XML identity: XML -> JSON -> XML")
    
    # Load a real TECHDOC XML file
    xml_file = Path("../techdoc/std.vocab.md")
    if not xml_file.exists():
        # Create test XML if file doesn't exist
        xml_content = '''<?xml version='1.0' encoding='utf-8'?>
<techdoc>
  <title>Test Document</title>
  <section name="Summary">
    <statement>This is a test statement.</statement>
  </section>
  <section name="Constraints">
    <statement id="T01" type="provable">All scripts MUST use proper error handling.</statement>
    <statement id="T02" type="heuristic">Code SHOULD be well-documented.</statement>
  </section>
</techdoc>'''
    else:
        # Convert MD to XML first to get test content
        md_content = xml_file.read_text(encoding="utf-8")
        ast = md_parse(md_content)
        xml_content = xml_serialize(ast)
    
    # XML -> JSON -> XML
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write(xml_content)
        xml_file1 = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        xml_file2 = f.name
    
    try:
        # Convert XML to JSON
        convertEncoding.convert_document(
            from_module="encodingXML",
            to_module="encodingJSON",
            input_path=xml_file1,
            output_path=json_file,
        )
        
        # Convert JSON back to XML
        convertEncoding.convert_document(
            from_module="encodingJSON",
            to_module="encodingXML",
            input_path=json_file,
            output_path=xml_file2,
        )
        
        # Compare original and final XML
        original_xml = normalize_xml(xml_content)
        final_xml = normalize_xml(Path(xml_file2).read_text(encoding="utf-8"))
        
        if original_xml == final_xml:
            print("✓ XML identity test PASSED")
            return True
        else:
            print("✗ XML identity test FAILED")
            print("Original XML:")
            print(original_xml)
            print("-" * 50)
            print("Final XML:")
            print(final_xml)
            return False
    
    finally:
        # Cleanup
        Path(xml_file1).unlink(missing_ok=True)
        Path(json_file).unlink(missing_ok=True)
        Path(xml_file2).unlink(missing_ok=True)


def test_json_identity() -> bool:
    """Test JSON roundtrip identity (JSON -> XML -> JSON)."""
    print("Testing JSON identity: JSON -> XML -> JSON")
    
    # Load a real TECHDOC JSON file or create test
    json_content = '''{
  "title": "Test Document",
  "sections": [
    {
      "name": "Summary",
      "content": [
        "This is a test statement."
      ]
    },
    {
      "name": "Constraints",
      "content": [
        {
          "id": "T01",
          "type": "provable",
          "content": "All scripts MUST use proper error handling."
        },
        {
          "id": "T02",
          "type": "heuristic",
          "content": "Code SHOULD be well-documented."
        }
      ]
    }
  ]
}'''
    
    # JSON -> XML -> JSON
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write(json_content)
        json_file1 = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        xml_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json_file2 = f.name
    
    try:
        # Convert JSON to XML
        convertEncoding.convert_document(
            from_module="encodingJSON",
            to_module="encodingXML",
            input_path=json_file1,
            output_path=xml_file,
        )
        
        # Convert XML back to JSON
        convertEncoding.convert_document(
            from_module="encodingXML",
            to_module="encodingJSON",
            input_path=xml_file,
            output_path=json_file2,
        )
        
        # Compare original and final JSON
        original_json = normalize_json(json_content)
        final_json = normalize_json(Path(json_file2).read_text(encoding="utf-8"))
        
        if original_json == final_json:
            print("✓ JSON identity test PASSED")
            return True
        else:
            print("✗ JSON identity test FAILED")
            print("Original JSON:")
            print(original_json)
            print("-" * 50)
            print("Final JSON:")
            print(final_json)
            return False
    
    finally:
        # Cleanup
        Path(json_file1).unlink(missing_ok=True)
        Path(xml_file).unlink(missing_ok=True)
        Path(json_file2).unlink(missing_ok=True)


def test_markdown_identity() -> bool:
    """Test Markdown roundtrip identity via JSON (MD -> JSON -> MD)."""
    print("Testing Markdown identity: MD -> JSON -> MD")
    
    # Load a real TECHDOC MD file
    md_file = Path("../techdoc/std.vocab.md")
    if not md_file.exists():
        print("⚠ Skipping MD identity test - std.vocab.md not found")
        return True
    
    md_content = md_file.read_text(encoding="utf-8")
    
    # MD -> JSON -> MD
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write(md_content)
        md_file1 = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json_file = f.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        md_file2 = f.name
    
    try:
        # Convert MD to JSON
        convertEncoding.convert_document(
            from_module="encodingMD",
            to_module="encodingJSON",
            input_path=md_file1,
            output_path=json_file,
        )
        
        # Convert JSON back to MD
        convertEncoding.convert_document(
            from_module="encodingJSON",
            to_module="encodingMD",
            input_path=json_file,
            output_path=md_file2,
        )
        
        # Compare original and final MD
        original_md = normalize_markdown(md_content)
        final_md = normalize_markdown(Path(md_file2).read_text(encoding="utf-8"))
        
        if original_md == final_md:
            print("✓ Markdown identity test PASSED")
            return True
        else:
            print("✗ Markdown identity test FAILED")
            print("Original MD (first 500 chars):")
            print(original_md[:500])
            print("-" * 50)
            print("Final MD (first 500 chars):")
            print(final_md[:500])
            return False
    
    finally:
        # Cleanup
        Path(md_file1).unlink(missing_ok=True)
        Path(json_file).unlink(missing_ok=True)
        Path(md_file2).unlink(missing_ok=True)


def test_full_cycle_identity() -> bool:
    """Test full cycle identity through all formats (XML -> JSON -> MD -> XML)."""
    print("Testing full cycle identity: XML -> JSON -> MD -> XML")
    
    # Create test XML
    xml_content = '''<?xml version='1.0' encoding='utf-8'?>
<techdoc>
  <title>Full Cycle Test</title>
  <section name="Summary">
    <statement>This is a test statement for full cycle.</statement>
  </section>
  <section name="Constraints">
    <statement id="T01" type="provable">All scripts MUST use proper error handling.</statement>
    <statement id="T02" type="heuristic">Code SHOULD be well-documented.</statement>
  </section>
  <section name="Data">
    <data language="json">{"test": true, "version": "1.0"}</data>
  </section>
</techdoc>'''
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # File paths
        xml_file1 = temp_path / "1.xml"
        json_file = temp_path / "2.json"
        md_file = temp_path / "3.md"
        xml_file2 = temp_path / "4.xml"
        
        # Write original XML
        xml_file1.write_text(xml_content, encoding="utf-8")
        
        # XML -> JSON -> MD -> XML
        convertEncoding.convert_document(
            from_module="encodingXML",
            to_module="encodingJSON",
            input_path=str(xml_file1),
            output_path=str(json_file),
        )
        
        convertEncoding.convert_document(
            from_module="encodingJSON",
            to_module="encodingMD",
            input_path=str(json_file),
            output_path=str(md_file),
        )
        
        convertEncoding.convert_document(
            from_module="encodingMD",
            to_module="encodingXML",
            input_path=str(md_file),
            output_path=str(xml_file2),
        )
        
        # Compare original and final XML
        original_xml = normalize_xml(xml_content)
        final_xml = normalize_xml(xml_file2.read_text(encoding="utf-8"))
        
        if original_xml == final_xml:
            print("✓ Full cycle identity test PASSED")
            return True
        else:
            print("✗ Full cycle identity test FAILED")
            print("Original XML:")
            print(original_xml)
            print("-" * 50)
            print("Final XML:")
            print(final_xml)
            return False


def main() -> None:
    """Run all identity tests."""
    print("Running TECHDOC identity tests (techdoc-encoding.spec E03)...")
    print("=" * 60)
    
    tests = [
        test_xml_identity,
        test_json_identity,
        test_markdown_identity,
        test_full_cycle_identity,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            import traceback
            traceback.print_exc()
            print()
    
    print("=" * 60)
    print(f"Identity tests: {passed}/{total} passed")
    
    if passed == total:
        print("All identity tests PASSED! ✓")
        sys.exit(0)
    else:
        print("Some identity tests FAILED! ✗")
        sys.exit(1)


if __name__ == "__main__":
    main()
