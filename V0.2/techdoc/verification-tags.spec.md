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

* D01 A Verification INDICATOR is a standardized annotation attached to a NORMATIVE ASSERTION describing the admissible method(s) of verification.

### General Rules

* V01 Verification INDICATORS MUST only appear in NORMATIVE ASSERTIONS. Ⓟ
* V02 A verification INDICATOR MUST NOT introduce or modify NORMATIVE meaning. Ⓗ
* V03 Each NORMATIVE ASSERTION SHOULD specify at most one verification INDICATOR. Ⓗ
* V04 Absence of a verification INDICATOR implies that the method of verification is unspecified. Ⓝ

### Structural Constraints

* V11 Each verification INDICATOR MUST have exactly one defining INDICATIVE STATEMENT fixing its meaning. Ⓟ
* V12 Verification INDICATORS MUST have disjoint semantics. Ⓟ

### Verification Guidance

* PROVABLE statements are typically validated via parsers, linters, or schema checks.
* TESTABLE statements are typically validated via executable test suites.
* EVALUATABLE statements are typically require instrumenting the artifact under test.
* HEURISTIC statements typically require human or AI-assisted review.
