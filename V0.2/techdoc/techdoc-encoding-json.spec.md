<!-- markdownlint-disable MD041 -->
## techdoc-encoding-json.spec: TECHDOC JSON Encoding Profile

### Summary

This document defines a JSON-based ENCODING profile for TECHDOCs.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [TECHDOC Structural Specification](techdoc-structural.spec.md)
* [TECHDOC Encoding Specification](techdoc-encoding.spec.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Specification

* J01 A TECHDOC MUST be represented as a single JSON object. Ⓟ
* J02 The top-level JSON object MUST contain:
  * `"title"`: string containing the TECHDOC name. Ⓟ
  * `"sections"`: array of SECTION objects. Ⓟ
* J03 All SECTION objects MUST contain:
  * `"name"`:string with the SECTION name. Ⓟ
* J04 NARRATIVE and ASSERTION SECTION objects MUST contain:
  * `"content"`: array of STATEMENTS. Ⓟ
* J05 NARRATIVE and INDICATIVE STATEMENTS MUST be represented as strings. Ⓟ
* J06 NORMATIVE STATEMENTS MUST be represented as objects containing:
  * `"id"`: string, the STATEMENT's unique identifier. Ⓟ
  * `"type"`: string, maps to the verification INDICATOR, Ⓟ
  * `"content"`: string, the statement text. Ⓟ
* J10 Data SECTION MUST contain the fields:
  * `"language"` : string, data language identifier (e.g. `yaml`, `json`). Ⓟ
  * `"data"`: string, containing the data. Ⓟ
* J40 SECTION ordering MUST be preserved. Ⓟ
* J41 STATEMENT ordering MUST be preserved. Ⓟ
