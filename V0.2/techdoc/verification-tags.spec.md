<!-- markdownlint-disable MD041 -->
## verification-tags.spec: Verification Indicators Specification

### Summary

Verification indicators describe *how* conformance to an assertion is to be evaluated, without contributing normative meaning themselves.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Document Vocabulary](document.vocab.md)
* [Verification Indicators Vocabulary](verification-tags.vocab.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Definitions

* D01 A VERIFICATION-INDICATOR is a standardized annotation attached to a NORMATIVE ASSERTION describing the admissible method(s) of verification.

### General Rules

* V01 VERIFICATION-INDICATORS MUST only appear in NORMATIVE ASSERTIONS.
* V02 A VERIFICATION-INDICATOR MUST NOT introduce or modify NORMATIVE meaning.
* V03 Each NORMATIVE ASSERTION MUST specify at most one VERIFICATION-INDICATOR.
* V04 Absence of a VERIFICATION-INDICATOR implies that the method of verification is unspecified.

### Structural Constraints

* V10 Each VERIFICATION-INDICATOR MUST be uniquely identifiable by a single symbol or token.
* V11 Each VERIFICATION-INDICATOR MUST have exactly one defining INDICATIVE STATEMENT fixing its meaning.
* V12 VERIFICATION-INDICATORS MUST have disjoint semantics.

### Verification Guidance (Informative)

* Ⓟ indicators are typically validated via parsers, linters, or schema checks.
* Ⓣ indicators are validated via executable test suites.
* Ⓗ indicators require human or AI-assisted review.
* Ⓝ indicators are exempt from verification tooling.
