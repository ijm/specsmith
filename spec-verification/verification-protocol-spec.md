<!-- markdownlint-disable MD041 -->
## verification-protocol-spec: Verification Protocol Specification

### Summary

This specification defines a structured, parsable protocol for reporting verification results of specification requirements. The protocol is designed to provide clear, machine-readable feedback for AI code generation loops while remaining human-readable for debugging and review.

### Scope and Intent

This specification provides a standardized output format for verification and test tools that validate specification compliance. It is intended for use by automated verification systems, AI feedback loops, and human reviewers.

### Metadata

```yaml
version: 1.0.0
```

### Imports and Inheritance

* This specification conforms to the Commonmark Markdown specification.
* Versioning, change tracking, and change logs are external, and conform to the meta-versioning-spec.
* This specification conforms to the BCP 14 keyword specification.
* The tag symbols Ⓟ, Ⓣ, Ⓔ, Ⓗ, and Ⓝ definition and usage conforms to the verification-tags-spec specification.
* The Metadata section conforms to the metadata-spec specification.

### Terminology and Conventions

* The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals.
* A **verification line** refers to a single line of protocol output.
* A **test name** identifies the specific verification being performed.
* A **source reference** identifies the source code or specification document and line number that engendered this verification.

### Functional Requirements

* Each verification line MUST follow the format: `{status} {test-name} {source-reference} [optional-message]`. Ⓟ
* A status MUST be one of: `PASS`, `INFO`, `WARN`, `FAIL`, `CRIT`, or `NIMP`; meaning Pass, Information, Warning, Failure (continue testing), Critical (abort testing), and Not Implemented (the verification is not implemented). Ⓟ
* A test name SHOULD use hyphenated-lowercase format but MAY use quoted strings for complex names. Ⓟ
* A source reference MUST follow the format `source-id:line-number`. Ⓟ
* A floor–target–ceiling triple MUST be in the format `(floor,target,ceiling)`. Ⓟ
* The source-id MUST match the source file name, or the specification name from its first-level heading. Ⓟ
* Optional messages MUST be enclosed in double quotes. Ⓟ
* Multiple verification lines for the same specification requirement are permitted. Ⓝ

### Structural Constraints

* Each verification line MUST be a single line with no embedded newlines. Ⓟ
* Fields MUST be separated by single space characters. Ⓟ
* The status field MUST be exactly one of the defined values in uppercase. Ⓟ
* Test names MUST contain only alphanumeric characters, hyphens, and underscores. Ⓟ

### Definitions

* **Status**: Result of the verification (PASS, INFO, WARN, FAIL, CRIT, NIMP).
* **Test Name**: Identifier for the specific verification being performed.
* **Source Reference**: Location identifier in format `source-id:line-number`.
* **Optional Message**: Additional context or error details in quoted format.

### Prohibited Elements

* Verification lines MUST NOT span multiple lines. Ⓟ
* Test names MUST NOT contain whitespace, or quotes. Ⓟ

### Example Output

```text
PASS heading-structure meta-generation-spec:15
FAIL missing-section meta-generation-spec:23 "Required section 'Verification' not found"
PASS api-response user-auth-spec:42
FAIL timeout-exceeded performance-spec:67 "Response time 5.2s exceeds limit 2.0s"
WARN performance-boundary api-spec:89 "Latency 150ms above target 100ms but below ceiling 200ms"
PASS code-clarity style-guide:128
NIMP subjective-assessment documentation-spec:56 "Manual review required"
```

### Verification

* **Ⓟ Provable items**:
  * Static checking SHOULD verify the that any protocol line emitted is valid:
    * Field count and separator consistency
    * Status value validity (PASS, INFO, WARN, FAIL, CRIT, NIMP)
    * Specification reference format.
    * Test name format compliance.
    * Quote matching in optional messages.
