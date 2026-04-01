<!-- markdownlint-disable MD041 -->
## verification-tags.vocab: Verification Indicators Vocabulary

### Summary

This specification defines a controlled vocabulary of Verification INDICATORS used to annotate NORMATIVE ASSERTIONS in TECHDOCs.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Document Vocabulary](document.vocab.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Verification INDICATOR Vocabulary

The following Verification INDICATORS are defined:

* (V01) PROVABLE implies that conformance can be established via static analysis, structural inspection, or deterministic logic (e.g. parsing, schema validation, keyword presence).
* (V02) TESTABLE implies that conformance can be established by executing one or more pass/fail style tests (unit, integration, or system-level).
* (V03) EVALUATABLE implies that conformance is determined by measuring a graded or continuous quantity against explicit acceptance criteria defined by the assertion (e.g. thresholds, ranges, or ordered comparisons).
* (V04) HEURISTIC implies that conformance is assessed via subjective judgment, expert review, or AI-assisted evaluation. Results are inherently non-deterministic.
* (V05) NOTATION implies that the assertion documents a constraint or convention that is not intended to be verified.
