
## meta-generation-spec: Specification Format for Composable Code Generation

### Summary

This meta-specification defines the structure, formatting, and verification expectations for generating code specifications intended to be consumed by an AI code generator or a junior developer. The generated specifications MUST be clear, structured, composable, and verifiable by human and AI.

### Scope and Intent

This meta-specefication governs how to construct other specifications. It is intended to be used as a prompt for an LLM to generate specification documents with standardized formatting, terminology, and content structure. The resulting specifications MUST be suitable for direct consumption by automated tools or developers, and SHOULD minimize ambiguity. Specifications documents SHOULD cover just one topic, component, or module.

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

* The generated specification is referred to simply as 'the specification'. This meta-specificaiton is always referred to as 'meta-specification'.
* The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals.

### Functional Requirements

* The specification MUST conform to the Commonmark Markdown specification.
* The specification MUST conform to the BCP 14 keyword specification.
* The tag symbols Ⓟ, Ⓣ, Ⓔ, and Ⓗ definition and usage MUST conform to the verification-tags-spec specification.
* The specification's metadata section MUST conform to the metadata-spec specification.
* The specification SHOULD be designed to be composable with other specifications (i.e., includeable, or copy-pasteable without modification). Ⓗ 
* The first section title in the document MUST be a level-2 heading (`##`) and MUST contain the name and title of the specification. Ⓟ
* The specification MUST include the following sub-sections, in order: Summary, Scope and Intent, Metadata, Imports and Inheritance, Terminology and Conventions, Functional Requirements, Structural Constraints, Definitions (Optional), Prohibited Elements, Example Output (Optional), and Verification. Ⓟ
* Each sub-section heading MUST be a level-3 heading (`###`). Ⓟ
* Each line item in the Functional Requirements, Structural Constraints, and Prohibited Elements sections SHOULD include one of the verification tags (Ⓟ, Ⓣ, Ⓔ, Ⓗ ) to indicate how compliance is to be determined. Ⓟ
* The "Imports and Inheritance" section MUST contain any and all referenced specifications. Ⓟ
* Referenced specifications MUST be identified by their exact title as it appears in their first-level heading. Ⓟ
* All inherited specifications MUST be followed. Ⓟ
* Minor specification conflicts, that is, those that will have no effect on the resultant build MUST be reported as a warning. All other inconsistencies or conflicts in or between specifications MUST be treated as terminal and reported as such. DO NOT attempt to find a resolution, or common compromise. Ⓗ 
* The “Verification” section MUST include instructions for verifying all tagged requirements. Ⓟ
* Outdated requirements MUST be either explicitly updated, replaced with MUST NOT, or removed entirely. Specifications MUST NOT retain deprecated elements. Ⓟ
* The specification MUST avoid ambiguous language and MUST use imperative voice. Ⓗ 
* Version control MUST be handled externally. Version information MAY appear in the metadata section for information use only. Ⓗ 

### Structural Constraints

* Bullet points MUST be used for all individual requirements. Ⓟ
* Inline code formatting MUST be used for all references to identifiers, file names, and code literals. Ⓟ
* Fenced code blocks (\`\`\`) MUST be used for all multi-line code examples. Ⓟ
* Each requirement tag (Ⓟ, Ⓣ, Ⓔ, Ⓗ ) MUST appear only on bullet point requirements, not on headings or section titles. Ⓟ
* Section headings MUST NOT be bolded. Bold MAY be used for section titles or emphasis within paragraphs. Ⓟ
* The Imports and Inheritance section SHOULD include the 'Commonmark Markdown', 'BCP 14 keyword', 'verification-tags-spec', and metadata-spec specifications, exactly as in this meta-specification.
* The Terminology and Conventions section MUST include the full BCP 14 boilerplate as specified. Ⓟ
* Specifications SHOULD prioritize human-readable formatting; specification parsing MUST NOT depend on layout beyond Markdown structural conventions. Ⓟ

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

* Specifications MUST NOT use vague terms such as “try to”, “ideally”, or “might”. Ⓟ
* Specifications MUST NOT omit any of the REQUIRED sections listed above. Ⓟ
* Specifications MUST NOT use BCP 14 keywords in lowercase or inconsistent capitalization. Ⓟ
* Specifications MUST NOT use narrative prose outside of the Summary and Scope and Intent sections. Ⓗ 

### Verification

* **Ⓟ Provable items**:
  Can be verified by static analysis of the Markdown structure. This includes checking:

  * Heading levels and their order
  * Presence of BCP 14 boilerplate
  * Proper tagging of bullet points
  * Correct use of inline formatting and fenced code blocks
    Tools: Markdown parsers, regex, or AST-style analysis of the output document.

* **Ⓣ Testable items**:
  N/A in this specification. The output is a static document.

* **Ⓔ Evaluatable items**:
  N/A in this specification. The output is a static document.

* **Ⓗ Heuristically Acceptable items**:
  Can be reviewed via human inspection, style tools, or AI analysis.



