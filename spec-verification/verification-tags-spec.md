<!-- markdownlint-disable MD041 -->
## verification-tags-spec: Verification Tags Specification

### Summary

This specification defines a standard set of verification tags used to annotate specification requirements for automated or manual validation. These tags are intended to indicate how compliance with a requirement can be verified and to facilitate tool-based parsing and analysis.

### Scope and Intent

This specification provides a controlled vocabulary for requirement-level verification tagging. It is intended for use in all specifications that conform to the Composable Code Generation meta-specification. The tags defined here MUST be used consistently and exclusively to indicate verifiability mode.

### Metadata

```yaml
version: 1.0.0
```

### Imports and Inheritance

* This specification conforms to the Commonmark Markdown specification.
* Versioning, change tracking, and change logs are external, and conform to the meta-versioning-spec.
* The Metadata section conforms to the meta-data-spec.
* This specification conforms to the BCP 14 keyword specification.
* The tag symbols Ⓟ, Ⓣ, Ⓔ, Ⓗ, and Ⓝ definition and usage conforms to the verification-tags-spec (this specification).

### Terminology and Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals.

The verification tags Ⓟ, Ⓣ, Ⓔ, Ⓗ, and Ⓝ are defined below use Unicode circled letters for ease of recognition and machine parsing.

### Functional Requirements

* All verification tags MUST be single Unicode circled letters characters. Ⓟ  
* Each tag MUST have a unique semantic meaning with no overlap. Ⓗ  
* Each requirement in a consuming specification SHOULD include only one and only one verification tag. Ⓗ  
* Tags SHOULD be placed at the end of a requirement bullet point. Ⓟ  
* The tags MUST be treated as semantic annotations and NOT as mere decoration. Ⓗ  
* New verification tags SHOULD be avoided, but if used they MUST:
  * Use a single Unicode circled letter not already in use. Ⓟ
  * Provide a clear name and normative description. Ⓟ
  * Provide Objective guidance on how compliance is to be verified. Ⓗ
* Undefined tags MUST be rejected by verification tools. Ⓟ

### Structural Constraints

* Each tag definition MUST include the symbol, name, and description. Ⓟ  
* Descriptions MUST be written in clear, normative, imperative language. Ⓗ  

### Verification Tag Definitions

* **Ⓟ — Provable**: The requirement can be verified via static analysis, structure parsing, or deterministic logic. Examples include formatting, file structure, keyword usage.
* **Ⓣ — Testable**: The requirement can be verified by running pass/fail tests (unit, integration, etc.).
* **Ⓔ — Evaluatable**: The requirement MUST include a floor–target–ceiling triple, defining the minimum acceptable value, the desired goal, and the maximum useful or plausible value of a continuous or graded measurement, such as performance, accuracy, or complexity.
* **Ⓗ — Heuristically Acceptable**: The requirement is assessed subjectively or fuzzily, by human review or AI-assisted style checking.
* **Ⓝ - Notation**: The requirement is a notation, annotation, or implementation detail that is not subject to verification.

### Prohibited Elements

* Verification tags MUST NOT be used for non-requirement prose. Ⓟ
* Tags MUST NOT be redefined, aliased, or extended within other specifications. Ⓟ
* Tags MUST NOT be applied to more than one requirement in the same line. Ⓟ

### Verification

* **Ⓟ Provable items**:
  SHOULD be validated via Markdown parsing and static checks. For example:
  * Tag format and placement (Unicode check, end-of-line detection)
  * Tag exclusivity and section placement
  * Order and structure of the tag definitions

* **Ⓗ Heuristically Acceptable items**:
  Clarity of definitions and semantic appropriateness SHOULD be evaluated by reviewers, style tooling, or AI.
