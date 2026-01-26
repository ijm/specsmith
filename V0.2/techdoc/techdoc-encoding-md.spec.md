<!-- markdownlint-disable MD041 -->
## TECHDOC Markdown Encoding Profile

### Summary

This document defines a Markdown-based ENCODING profile for TECHDOCs.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [TECHDOC Structural Specification](techdoc-core.spec.md)
* [TECHDOC Encoding Specification](techdoc-encoding.spec.md)
* The CommonMark Markdown specification.

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Specification

* M01 The TECHDOC's name MUST be encoded as a level 2 heading.
* M02 Each TECHDOC SECTION name MUST be encoded as a level 3 heading.
* M03 SECTION order in the document MUST correspond to the order of headings.
* M10 A Data SECTION MUST be encoded as a fenced code block immediately following its heading.
* M11 The fenced block of a Data SECTION MUST declare a data language identifier (e.g. `yaml`, `json`).
* M20 A NARRATIVE SECTION MUST be encoded as freeform Markdown content following its heading.
* M30 An ASSERTION SECTION MUST be encoded as a Markdown list.
* M31 Each list item corresponds to exactly one ASSERTION STATEMENT.
* M40 Each ASSERTION STATEMENT MUST begin with a unique identifier followed by a space.
* M41 Verification indicators, if present, MUST appear at the end of the list item.
