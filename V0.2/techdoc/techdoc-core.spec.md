<!-- markdownlint-disable MD041 -->
## techdoc-core.spec: TECHDOC Core Structural Specification

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
* T02 A reader or processor MUST NOT introduce, assume, or invent DEFINED-TERMs beyond those explicitly defined in-scope.

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

#### Common STE Rules

* E01 A STATEMENT SHOULD be expressed as a simple declarative sentence.
* E02 A STATEMENT MUST be written so that it has exactly one plausible interpretation within the scope of the document..
* E03 A STATEMENT SHOULD NOT use ambiguous or weakly modal language (e.g. “try to”, “ideally”, “might”).
* E04 A STATEMENT MUST NOT rely on implied context, unstated conditions, or assumed prior steps.
* E05 A STATEMENT SHOULD NOT contain multiple coordinated actions unless their order and dependence are explicit.
