<!-- markdownlint-disable MD041 -->
## metadata-spec: Metadata Section Specification

### Summary

Defines the required structure, format, and content of the Metadata section in composable code generation specifications. Ensures that metadata is machine-readable, human-auditable, and safe for use in automated pipelines.

### Scope and Intent

This specification standardizes how metadata is represented, encoded, and validated within generated specifications. It is intended to facilitate tooling, indexing, validation, and versioning of composable specification documents.

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

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals. Ⓟ

### Functional Requirements

* The Metadata section MUST appear directly after the Scope and Intent section. Ⓟ
* The Metadata section MUST contain a single fenced code block of type `yaml`. Ⓟ
* Each metadata field MUST use explicit lowercase YAML 1.2 compatible scalar values. Ⓟ
* Custom fields MAY be included, but MUST NOT interfere with required field names. Ⓗ
* The YAML format MUST conform to the safe subset defined in the meta-specification. Ⓟ

### Structural Constraints

* The metadata MUST be placed inside a fenced block with the language identifier `yaml`. Ⓟ
* The fenced block MUST NOT use front-matter delimiters (i.e., `---`). Ⓟ
* The YAML block MUST NOT contain anchors, aliases, or non-scalar keys. Ⓟ
* Each metadata field SHOULD appear on its own line. Ⓗ

### Prohibited Elements

* The Metadata section MUST NOT use YAML front-matter (`---`). Ⓟ
* The Metadata section MUST NOT include YAML features such as anchors, references, or tags. Ⓟ
* Metadata fields MUST NOT use ambiguous or implicit typing (e.g., `yes`, `01`). Ⓟ

### Example Output (Optional)

```yaml
version: 1.2.3
author: Jane Doe
last_updated: 2025-04-10
```

### Verification

**Ⓟ Provable items**:

* Use of ` ```yaml ` fenced block format
* Disallowed YAML features (anchors, aliases, front-matter)

**Ⓗ Heuristically Acceptable items**:

* Relevance and accuracy of field values
* Naming consistency of tags and authors

**Ⓣ Testable items**: N/A

**Ⓔ Evaluatable items**: N/A
