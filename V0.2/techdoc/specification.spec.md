<!-- markdownlint-disable MD041 -->
## (Meta) Specification Specification

### Summary

This document defines the constraints for documents that define specifications.

### Imports & Inheritance

This document inherits from:

* [TECHDOC Specification](techdoc.spec.md)

This conforms to :

* [Specification Specification](specification.spec.md) (Itself)

### Terminology and Conventions

* D01 A SPECIFICATION is a TECHDOC whose NORMATIVE STATEMENTS define constraints on artifacts, processes, or other documents.
* S14 Definition SECTIONS such as Terminology, Conventions, Vocabulary, etc SHOULD contain only INDICATIVE STATEMENTS.
* S15 Constraint SECTIONS such as Functions, Structural, etc SHOULD contain only NORMATIVE STATEMENTS.


### Functional Constraints

* F02 A SPECIFICATION SHOULD address exactly one topic, component, or module.
* F03 A SPECIFICATION SHOULD be composable with other specifications without modification.
* F04 All conformance requirements MUST be expressed exclusively as NORMATIVE STATEMENTS.
* F05 All external SPECIFICATIONS relied upon MUST be listed in an Imports & Inheritance SECTION.
* F06 Version control MUST be handled externally; version identifiers, if present, MUST be informational only.
* F07 Deprecated requirements MUST NOT appear; removal or explicit prohibition is required.

#### Conflict Handling

* F11 Any conflict between constraints that affects conformance MUST be treated as terminal.
* F12 Conflicts that do not affect admissibility MUST be reported as warnings.
* F13 A SPECIFICATION MUST NOT attempt to resolve or reconcile conflicting inherited constraints.

### Structural Constraints

* A SPECIFICATION DOCUMENT MUST contain the following SECTIONS, in the order listed:
  * S11 Summary
  * S12 Scope (OPTIONAL)
  * S13 Imports & Inheritance (OPTIONAL)
  * S14 Definition SECTIONS (OPTIONAL)
  * S15 Constraint SECTIONS
  * S16 Explicitly Prohibited Elements (OPTIONAL)
  * S17 Verification Methodologies
