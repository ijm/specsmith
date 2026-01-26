<!-- markdownlint-disable MD041 -->
## TECHDOC Core Structural Specification

### Summary

A TECHDOC consists of an ordered collection of named NARRATIVE, ASSERTION, or Data SECTIONS. ASSERTIONS can be INDICATIVE or NORMATIVE. Only NORMATIVE ASSERTIONS impose conformance, verification or evaluation constraints.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Document Vocabulary](document.vocab.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Definitions

* D01 A Data SECTION contains structured information, whose specific structure is unconstrained by this specification.

### Functional Constraints

#### General

* T01 A TECHDOC MUST contain an ordered collection of named NARRATIVE, ASSERTION, or Data SECTIONS.

#### Sections

* S01 A NARRATIVE SECTION SHOULD contain NARRATIVE STATEMENTS.
* S02 A NARRATIVE SECTION SHOULD NOT contain ASSERTION STATEMENTS.
* S03 Any assertive statements expressed in NARRATIVE SECTIONS are **informative only** and MUST NOT be treated as ASSERTIONS for the purposes of compliance or verification.

#### Assertions

* A01 An ASSERTION SECTION MUST NOT contain NARRATIVE STATEMENTS.
* A02 An INDICATIVE SECTION MUST contain only INDICATIVE STATEMENTS.
* A03 A NORMATIVE SECTION MUST contain only NORMATIVE STATEMENTS.
* A04 Each ASSERTION STATEMENT MUST have a unique identifier within the document.
* A05 INDICATIVE ASSERTIONS MUST NOT impose conformance constraints.
* A06 A NORMATIVE ASSERTION MUST contain at least one NORMATIVE indicator (e.g. MUST or SHOULD NOT)
