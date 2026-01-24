<!-- markdownlint-disable MD041 -->
## meta-generation-spec: Specification Format for Composable Code Generation

### Summary

This meta-specification defines the structure, formatting, and verification expectations for generating code specifications intended to be consumed by an AI code generator or a junior developer. The generated specifications MUST be clear, structured, composable, and verifiable by human and AI.

### Scope and Intent

This meta-specification governs how to construct other specifications. It is intended to be used as a prompt for an LLM to generate specification documents with standardized formatting, terminology, and content structure. The resulting specifications MUST be suitable for direct consumption by automated tools or developers, and SHOULD minimize ambiguity. Specifications documents SHOULD cover just one topic, component, or module.

### Metadata

```yaml
version: 1.0.0
```

### Imports and Inheritance

* This specification conforms to the following specifications:
  * Commonmark Markdown,
  * BCP 14 keyword,
  * verification-tags-spec.md,
  * metadata-spec.md,
  * versioning-spec.md

### Terminology and Conventions

* The specification to be generated is referred to as 'the specification'. This meta-specification is and MUST be referred to as 'meta-specification'.

### Functional Requirements

* F01: Specification names SHOULD be in slug-case, and MUST NOT contain white space. Ⓟ
* F02: The specification SHOULD be designed to be composable with other specifications (i.e., includable, or copy-pasteable without modification). Ⓗ
* F03: Each line item in the Functional Requirements, Structural Constraints, and Prohibited Elements sections SHOULD include one of the verification tags (Ⓟ, Ⓣ, Ⓔ, Ⓗ, Ⓝ) to indicate how compliance is to be determined. Ⓟ
* F04: The "Imports and Inheritance" section MUST contain any and all referenced specifications. Ⓟ
* F05: Minor specification conflicts, that is, those that will have no effect on the resultant build MUST be reported as a warning. All other inconsistencies or conflicts in or between specifications MUST be treated and reported as terminal. DO NOT attempt to find a resolution, or common compromise. Ⓗ
* F06: The “Verification” section MUST include instructions for verifying all tagged requirements. Ⓟ
* F07: Outdated requirements MUST be either explicitly updated, replaced with MUST NOT, or removed entirely. Specifications MUST NOT retain deprecated elements. Ⓟ
* F08: The specification MUST avoid ambiguous language and MUST use imperative voice. Ⓗ
* F09: Version control MUST be handled externally. Version information MAY appear in the metadata section for information use only. Ⓗ

### Structural Constraints

* S01: Specifications SHOULD prioritize human-readable formatting; specification parsing MUST NOT depend on layout beyond Markdown structural conventions. Ⓟ
* S02: Specifications SHOULD include the 'Commonmark Markdown', 'BCP 14 keyword', 'verification-tags-spec', and metadata-spec specifications. Ⓟ
* Sections:
  * S11: The first section title in the document MUST be a level-2 heading (`##`) and MUST contain the name and title of the specification. Ⓟ
  * S12: Sub-sections SHOULD be level-3 headings ('###'). Ⓟ
  * S13: The specification MUST include the following sub-sections, in order: Summary, Scope and Intent, Metadata, Imports and Inheritance, Terminology and Conventions, Functional Requirements, Structural Constraints, Definitions (Optional), Prohibited Elements, Example Output (Optional), and Verification. Ⓟ
* Styling:
  * S21: Bolding and emphasis MUST NOT be used outside narrative sections. Ⓟ
  * S22: Inline code formatting (`\`) MUST be used for all references, identifiers, file names, and code literals. Ⓟ
  * S23: Fenced code blocks (\`\`\`{language}) MUST be used for all multi-line code examples, and MUST include the language identifier. Ⓟ
* Individual specification points:
  * S31: MUST be formatted as bullet points (`*`) followed by a line identifier, and a colon. Ⓟ
  * S32: MAY be a multi-line bullet point, and MAY include additional formatting.
  * S33: Verification tags (Ⓟ, Ⓣ, Ⓔ, Ⓗ, Ⓝ) MUST appear on bullet specification points. Ⓟ
  * S34: Line identifiers MUST be unique within the specification, but do not need to be sequentially.

### Definitions

* **Summary**: Brief overview of the specification’s purpose and scope.
* **Scope and Intent**: Clarifies intended use, target audience, and boundaries.
* **Metadata**: Information about the specification (e.g., version, tags).
* **Imports and Inheritance**: Lists external specifications that this document conforms to or uses.
* **Terminology and Conventions**: Defines key terms, naming rules, and interpretations.
* **Functional Requirements**: Lists normative behaviors, features, or expectations.
* **Structural Constraints**: Defines formatting, layout, and document structure rules.
* **Definitions**: Provides formal descriptions of section-level or domain-specific terms or concepts.
* **Prohibited Elements**: Lists patterns or constructs explicitly disallowed.
* **Example Output**: Demonstrates compliant output or expected results.
* **Verification**: Describes how compliance with each requirement is determined.

### Prohibited Elements

* P01: Specifications MUST NOT use vague terms such as “try to”, “ideally”, or “might”. Ⓟ
* P02: Specifications MUST NOT use narrative prose outside of the Summary and Scope and Intent sections. Ⓗ

### Verification

* **Ⓟ Provable items**: Can be verified by static analysis of the Markdown structure. This includes checking:
  * Heading levels and their order
  * Proper tagging of bullet points
  * Correct use of inline formatting and fenced code blocks
  * Tools: Markdown parsers, regex, or AST-style analysis of the output document.
* **Ⓣ Testable items**: N/A
* **Ⓔ Evaluatable items**: N/A
* **Ⓗ Heuristically Acceptable items**:
  * Can be reviewed via human inspection, style tools, or AI analysis.
