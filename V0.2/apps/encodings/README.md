# TECHDOC Encoding Converter

Tools for converting TECHDOC specification documents between multiple serial document (not language) encodings (Markdown, JSON, XML) using a shared abstract syntax tree (AST) representation.

## Usage

Convert between formats using the CLI:

```bash
python convertEncoding.py -f encodingMD -t encodingJSON -i doc.md -o doc.json
python convertEncoding.py -f encodingJSON -t encodingXML -i doc.json -o doc.xml
python convertEncoding.py -f encodingXML -t encodingMD -i doc.xml -o doc.md
```
