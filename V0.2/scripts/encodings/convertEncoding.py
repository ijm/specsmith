#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TECHDOC Encoding Converter

A command-line tool to convert TECHDOC documents between different encodings
(Markdown, JSON, XML) using a shared abstract syntax tree representation.

Usage:
    python convertEncoding.py -f fromModule -t toModule -i infile -o outfile
"""

import argparse
import importlib
import sys
from pathlib import Path
from typing import Any

from ast_nodes import Techdoc


class ConversionError(Exception):
    """Exception raised during conversion process."""


def load_encoding_module(module_name: str) -> Any:
    """
    Dynamically load an encoding module.
 
    Raises:
        ConversionError: If module loading fails
    """
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError as e:
        raise ConversionError(f"Failed to load encoding module '{module_name}': {e}") from e


def validate_encoding_module(module: Any, module_name: str) -> None:
    """
    Validate that the encoding module has required functions.

    Raises:
        ConversionError: If required functions are missing
    """
    required_functions = ["parse", "serialize"]
    
    for func_name in required_functions:
        if not hasattr(module, func_name):
            raise ConversionError(
                f"Encoding module '{module_name}' missing required function '{func_name}'"
            )


def read_input_file(input_path: str) -> str:
    """
    Read content from input file.
    
    Raises:
        ConversionError: If file reading fails
    """
    try:
        path = Path(input_path)
        if not path.exists():
            raise ConversionError(f"Input file does not exist: {input_path}")
        
        if not path.is_file():
            raise ConversionError(f"Input path is not a file: {input_path}")
        
        return path.read_text(encoding="utf-8")
    except OSError as e:
        raise ConversionError(f"Failed to read input file '{input_path}': {e}") from e


def write_output_file(output_path: str, content: str) -> None:
    """
    Write content to output file.
 
    Raises:
        ConversionError: If file writing fails
    """
    try:
        path = Path(output_path)
        path.write_text(content, encoding="utf-8")
    except OSError as e:
        raise ConversionError(f"Failed to write output file '{output_path}': {e}") from e


def validate_format(content: str, module_name: str) -> None:
    """
    Perform minimal validation of document format.
    
    Raises:
        ConversionError: If format validation fails
    """
    # This is a minimal validation - just check if the content can be parsed
    # without raising an exception. More sophisticated validation can be added later.
    try:
        module = load_encoding_module(module_name)
        module.parse(content)
    except Exception as e:
        raise ConversionError(f"Format validation failed for {module_name}: {e}") from e


def convert_document(
    from_module: str, to_module: str, input_path: str, output_path: str
) -> None:
    """
    Convert a TECHDOC document from one encoding to another.
    
    Raises:
        ConversionError: If conversion fails
    """
    source_module = load_encoding_module(from_module)
    target_module = load_encoding_module(to_module)
    
    validate_encoding_module(source_module, from_module)
    validate_encoding_module(target_module, to_module)
    
    input_content = read_input_file(input_path)
    
    validate_format(input_content, from_module)
    
    try:
        ast = source_module.parse(input_content)
    except Exception as e:
        raise ConversionError(f"Failed to parse input document: {e}") from e
    
    if not isinstance(ast, Techdoc):
        raise ConversionError("Parser did not return a Techdoc object")
    
    try:
        output_content = target_module.serialize(ast)
    except Exception as e:
        raise ConversionError(f"Failed to serialize output document: {e}") from e
    
    write_output_file(output_path, output_content)


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description="Convert TECHDOC documents between different encodings",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -f encodingMD -t encodingJSON -i doc.md -o doc.json
  %(prog)s -f encodingJSON -t encodingXML -i doc.json -o doc.xml
  %(prog)s -f encodingXML -t encodingMD -i doc.xml -o doc.md
        """.strip(),
    )
    
    parser.add_argument("-f", "--from", required=True,
        help="Source encoding module (e.g., encodingMD, encodingJSON, encodingXML)",
    )
    
    parser.add_argument("-t", "--to", required=True,
        help="Target encoding module (e.g., encodingMD, encodingJSON, encodingXML)",
    )
    
    parser.add_argument("-i", "--input", required=True,
        help="Input file path",
    )
    
    parser.add_argument("-o", "--output", required=True,
        help="Output file path",
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0",
    )
    
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        convert_document(
            from_module=getattr(args, "from"),
            to_module=args.to,
            input_path=args.input,
            output_path=args.output,
        )
        print(f"Successfully converted {args.input} to {args.output}")
    except ConversionError as e:
        print(f"Conversion error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nConversion interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
