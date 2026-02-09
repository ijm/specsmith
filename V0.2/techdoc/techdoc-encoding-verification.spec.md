<!-- markdownlint-disable MD041 -->
## techdoc-verification-encoding.spec: TECHDOC Verification Encoding Specification

### Summary

This specification defines an abstract ENCODING for representing the verification-relevant semantics of NORMATIVE ASSERTIONS in a TECHDOC.
The verification encoding makes explicit the evaluative structure implicitly defined by each NORMATIVE ASSERTION, without introducing, modifying, or strengthening normative meaning.

This encoding is lossy with respect to NARRATIVE, INDICATIVE, and IMPERATIVE STATEMENTS and is a projection of the normative structure.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Document Vocabulary](document.vocab.md)
* [Verification Indicators Vocabulary](verification-tags.vocab.md)
* [TECHDOC Core Structural Specification](techdoc-core.spec.md)
* [TECHDOC Encoding Specification](techdoc-encoding.spec.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Definitions

* D01 A VERIFICATION ENCODING is an ENCODING that represents NORMATIVE ASSERTIONS in terms of their evaluative structure. It is a projection of the normative structure.
* D02 An AXIS classifies the kind of evaluation implicitly defined by a NORMATIVE ASSERTION.
* D03 A MEASURE describes how the subject of an AXIS is evaluated or observed.
* D04 An ADMISSIBLE region is the subset of AXIS outcomes that satisfy a NORMATIVE ASSERTION.

### Axis Examples

Examples of AXIS types:

* Metric - Evaluation yields a numeric value (with a defined unit or metric).
e.g. "Must weigh less than 5kg"
* Categorical - Evaluation yields qualitative or logical classification (Boolean, Fuzzy, Multi-valued, etc.). e.g. "Must be false"
* Set - Membership evaluation in a defined set. e.g. "Must be in the approved list"
* Ordering - Relative ordering or precedence within a sequence. e.g. "Must come before the deadline"
* Structural - Compositional or derivational relationships between entities. e.g.
"Must be derived from source A"

### Required Components per Encoded Assertion

Each encoded NORMATIVE ASSERTION MUST contain the fields:

* E10 `id` - the identifier of the source NORMATIVE ASSERTION.
* E11 `indicator` - the associated VERIFICATION-INDICATOR.
* E12 `axis` - exactly one AXIS type.
* E13 `subject` - the (sub-) entity being evaluated.

Each encoded NORMATIVE ASSERTION MAY if needed contain the fields:

* E14 `measure` - the MEASURE - method or procedure for evaluation.
* E15 `admission` - the ADMISSIBLE REGION that is the set of acceptable outcomes.
* E16 `narrative` - the narrative component of the statement if present

### Conditional Requirements by Verification Indicator

#### Provable, Testable, Evaluatable (Ⓟ Ⓣ Ⓔ)

* V20 A MEASURE MUST be explicitly defined for Ⓟ Ⓣ Ⓔ statements.
* V21 An ADMISSIBLE REGION MUST be explicitly defined for Ⓟ Ⓣ Ⓔ statements.

#### Heuristic (Ⓗ)

* V30 A MEASURE SHOULD be described, but MAY be informal for Ⓗ statements.
* V31 An ADMISSIBLE REGION SHOULD be described, but MAY be informal for Ⓗ statements.

#### Notation (Ⓝ)

* V40 A MEASURE MAY be omitted for Ⓝ statements.
* V41 An ADMISSIBLE REGION MAY be omitted for Ⓝ statements.
* V42 The ASSERTION MUST NOT claim evaluability or verification for Ⓝ statements.

### Structural Constraints

### Admissibility and Round-Trip Constraints

* V61 Conversion from TECHDOC → VERIFICATION ENCODING → TECHDOC MUST preserve:
  * the set of NORMATIVE ASSERTIONS,
  * their identifiers,
  * their VERIFICATION-INDICATORS,
  * and their normative meaning.
* V62 Natural language realization MAY differ on round-trip, but semantic equivalence MUST be preserved.


