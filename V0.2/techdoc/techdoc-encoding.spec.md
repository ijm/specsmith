<!-- markdownlint-disable MD041 -->
## techdoc-encoding.spec: TECHDOC Encoding Specification

### Summary

This specification defines the abstract requirements for an ADMISSIBLE ENCODING of a TECHDOC. Concrete encoding formats (e.g. Markdown, XML, JSON) are defined in separate Profile specifications.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [TECHDOC Structural Specification](techdoc-core.spec.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Local Definitions

* D01 An ENCODING is a concrete representation of a TECHDOC in some format.

### Admissibility Constraints

* E01 The interpretation of an ENCODING MUST be ADMISSIBLE as a TECHDOC. Ⓟ
* E02 An ENCODING MUST NOT claim to be canonical. Ⓟ
* E03 All ENCODINGS MUST be interchangeable. That is, conversion from ENCODING X to ENCODING Y and back to ENCODING X MUST preserve all TECHDOC information. Ⓣ
* E04 An ENCODING MUST NOT infer, synthesize, or reinterpret NORMATIVE meaning. Ⓟ
* An ENCODING MUST preserve:
  * E10 all SECTIONS with their names. Ⓟ
  * E11 SECTION and STATEMENT ordering Ⓟ
  * E12 All STATEMENT and verification INDICATORS Ⓟ
  * E13 all textual or data content Ⓟ
* E31 An ENCODING MUST NOT introduce additional ASSERTIONs or NARRATIVE statements. Ⓟ
* E32 Any metadata added by an encoding for transport or tooling purposes MUST be explicitly non-semantic and MUST be removable without information loss. Ⓟ
