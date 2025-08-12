## verification-protocol-spec: Verification Protocol Specification

### Summary

This specification defines a structured, parseable protocol for reporting verification results of specification requirements. The protocol is designed to provide clear, machine-readable feedback for AI code generation loops while remaining human-readable for debugging and review.

### Scope and Intent

This specification provides a standardized output format for verification tools that validate specification compliance. It is intended for use by automated verification systems, AI feedback loops, and human reviewers. The protocol MUST support all verification tag types defined in the verification-tags-spec and MUST be parseable by both humans and machines.

### Metadata

```yaml
version: 1.0.0
```

### Imports and Inheritance

* This specification conforms to the Commonmark Markdown specification.
* This specification conforms to the BCP 14 keyword specification.
* The tag symbols Ⓟ, Ⓣ, Ⓔ, and Ⓗ definition and usage conforms to the verification-tags-spec specification.
* The Metadata section conforms to the metadata-spec specification.

### Terminology and Conventions

* The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals.
* A **verification line** refers to a single line of protocol output.
* A **test name** identifies the specific verification being performed.
* A **specification reference** identifies the source specification and line number being verified.

### Functional Requirements

* Each verification line MUST follow the format: `{verification-tag} {status} {test-name} {specification-reference} [optional-message]`. Ⓟ
* The verification tag MUST be one of: `P`, `T`, `E`, or `H` corresponding to the verification-tags-spec definitions. Ⓟ
* The status MUST be one of: `PASS`, `INFO`, `WARN`, `FAIL", `CRIT`, or `NIMP` (not implemented). Ⓟ
* The test name SHOULD use hyphenated-lowercase format but MAY use quoted strings for complex names. Ⓟ
* The specification reference MUST follow the format `specification-id:line-number`. Ⓟ
* The specification-id MUST match the specification name from its first-level heading. Ⓟ
* The line number MUST reference the specific line in the specification document being verified. Ⓟ
* Optional messages MUST be enclosed in double quotes if they contain spaces or special characters. Ⓟ
* Each verification line MUST be terminated with a newline character. Ⓟ
* Multiple verification lines for the same specification requirement are permitted. Ⓟ
* Verification lines MUST be emitted in the order tests are executed. Ⓟ

### Structural Constraints

* Each verification line MUST be a single line with no embedded newlines. Ⓟ
* Fields MUST be separated by single space characters. Ⓟ
* The verification tag MUST be exactly one character. Ⓟ
* The status field MUST be exactly one of the four defined values in uppercase. Ⓟ
* Test names without quotes MUST contain only alphanumeric characters, hyphens, and underscores. Ⓟ
* Quoted test names MUST escape internal double quotes with backslash. Ⓟ
* The specification reference MUST contain exactly one colon separator. Ⓟ
* Line numbers MUST be positive integers. Ⓟ
* Optional messages MUST appear after the specification reference, separated by a space. Ⓟ

### Definitions

* **Verification Tag**: Single character indicating the verification method (P, T, E, H).
* **Status**: Result of the verification (PASS, INFO, WARN, FAIL, CRIT, NIMP).
* **Test Name**: Identifier for the specific verification being performed.
* **Specification Reference**: Location identifier in format `spec-id:line-number`.
* **Optional Message**: Additional context or error details in quoted format.

### Prohibited Elements

* Verification lines MUST NOT span multiple lines. Ⓟ
* Status values MUST NOT be in lowercase or mixed case. Ⓟ
* Specification references MUST NOT omit the line number. Ⓟ
* Test names MUST NOT contain spaces unless quoted. Ⓟ
* Optional messages MUST NOT be included without quotes if they contain spaces. Ⓟ

### Example Output

```
P PASS heading-structure meta-generation-spec:15
P FAIL missing-section meta-generation-spec:23 "Required section 'Verification' not found"
T PASS api-response user-auth-spec:42
T FAIL timeout-exceeded performance-spec:67 "Response time 5.2s exceeds limit 2.0s"
E WARN performance-boundary api-spec:89 "Latency 150ms above target 100ms but below ceiling 200ms"
H PASS code-clarity style-guide:128
H NIMP subjective-assessment documentation-spec:56 "Manual review required"
```

### Verification

* **Ⓟ Provable items**:
  Can be verified by parsing each line and checking:
  * Field count and separator consistency
  * Verification tag validity (P, T, E, H)
  * Status value validity (PASS, INFO, WARN, FAIL, CRIT, NIMP)
  * Specification reference format (contains exactly one colon)
  * Test name format compliance
  * Quote matching in optional messages

* **Ⓣ Testable items**:
  N/A in this specification. The output is a structured text format.

* **Ⓔ Evaluatable items**:
  N/A in this specification. The output is a structured text format.

* **Ⓗ Heuristically Acceptable items**:
  Test name clarity and message usefulness can be evaluated by human review.
