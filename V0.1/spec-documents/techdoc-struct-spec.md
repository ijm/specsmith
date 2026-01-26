<!-- markdownlint-disable MD041 -->
## techdoc-structural-spec: Technical Document Structural Specification

### Summary

This specification defines the abstract structure of a technical document (`techdoc`), its sections, and its assertion model. It provides the canonical Markdown form and mappings to XML and JSON. The structure is format-agnostic: content may be authored in Markdown and transformed losslessly into XML or JSON, then back again.

### Scope and Intent

This specification governs the structural layout of technical documents in this system. It separates content into three semantic regions: NARRATIVE, ASSERTIONS, and data. ASSERTIONS are further split into INDICATIVE (“what is”) and NORMATIVE (“what ought to be”) statements.

This specification does **not** define formatting rules. It defines the only the underlying document model shared across Markdown, XML, and JSON forms.

### Metadata

```yaml
version: 1.0.0
```

### Imports and Inheritance

* This specification conforms to:

  * Commonmark Markdown,
  * BCP 14 keyword specification,
  * verification-tags-spec,
  * metadata-spec,
  * versioning-spec.

### Terminology and Conventions

* a NARRATIVE: Unstructured explanatory text. It may include reasoning, context, motivation, or discussion. It contains no formal statements and carries no verification tag.
* an ASSERTION: A structured, single-sentence statement appearing in an assertions section. Assertions come in two kinds and must be individually identifiable.
* an INDICATIVE statement: An assertion describing *what is*. It expresses definitions, descriptive facts, inclusions, or structural truths. It MUST NOT contain a verification tag.
* a NORMATIVE statement: An assertion describing *what ought to be*. It expresses requirements, constraints, obligations, or permissions. It MUST include exactly one verification tag.

### Functional Requirements

* F01: A technical document MUST consist of only: NARRATIVE, ASSERTION, and data sections. Ⓟ
* F03: Each data section MUST contain structured data but MAY be in any appropriate serialization.
* F04: NARRATIVE sections MUST contain freeform Markdown text and MUST NOT contain structured ASSERTIONS. Ⓟ
* F05: ASSERTION sections MUST contain a list of indicative or normative statements, which MAY be freely interleaved. Ⓟ

* F06: Normative assertions MUST include exactly one verification tag. Ⓟ
* F07: Indicative assertions MUST NOT include a verification tag. Ⓟ
* F08: The XML and JSON representations MUST preserve ordering of all elements. Ⓟ
* F09: Conversions among Markdown, XML, and JSON MUST be lossless with respect to information content (not formatting). Ⓗ
* F10: Narrative text MUST be preserved verbatim except for normalization of surrounding whitespace during round-trip conversions. Ⓗ

* F04: When using Markdown:
  * F07: Data sections must use a fenced data block, such as `yaml`, to encapsulate and indicate the data format. Ⓟ
  * F06: Verification tags MUST be unicode circled letters such as `Ⓟ`, `Ⓣ`, `Ⓔ`, `Ⓗ`, or `Ⓝ`. Ⓟ
  * F07: Verification tags MUST appear at the end of the assertion statement. Ⓟ
  * F08: ASSERTION section MUST contain only bullet items with verification tags. Ⓟ
  * F09: Each bullet item MUST start with a line identifier followed by a colon and space, then the assertion text. Ⓟ

### Structural Constraints

* S01: The canonical Markdown representation MUST use level-2 section headings `## Data`, `## Narrative`, and `## Assertions`. Ⓟ
* S02: The `data` section MUST contain exactly one fenced YAML block and MUST NOT contain additional Markdown structures. Ⓟ
* S03: The `narrative` section MAY contain any Commonmark-compatible Markdown content. Ⓗ
* S04: The `assertions` section MUST encode each assertion as a bullet item containing a line identifier and statement text. Ⓟ
* S05: Normative bullet items MUST end with a verification tag symbol. Ⓟ
* S06: XML representation MUST be of the form:

  * `<techdoc>` root element
  * `<data name="meta">…</data>` containing YAML text
  * `<narrative format="markdown">…</narrative>`
  * `<assertions>` containing interleaved `<indi>` and `<norm>` elements
    Ⓟ
* S07: JSON representation MUST be of the form:

  ```json
  {
    "data": { "...": "..." },
    "narrative": "markdown string",
    "assertions": [
      { "type": "indi", "name": "...", "text": "..." },
      { "type": "norm", "name": "...", "tag": "P", "text": "..." }
    ]
  }
  ```

  Ⓟ
* S08: The XML and JSON forms MUST contain no fields or elements not present in this specification, except for explicit extensions defined in other specifications. Ⓗ

### Definitions (Optional)

* **Data section**: Structured key–value metadata. In Markdown this is a fenced YAML block; in XML and JSON, parsed key–value mappings.
* **Narrative section**: Unstructured textual content. Treated as opaque by tooling except during Markdown rendering.
* **Indicative assertion**: Declarative or definitional item documenting facts or included constraints.
* **Normative assertion**: Requirement or obligation annotated with a verification tag.
* **Verification tag**: A single Unicode circled letter in Markdown, mapped to a compact code (`"P"`, `"T"`, `"E"`, `"H"`, `"N"`) in XML/JSON.

### Prohibited Elements

* P01: Assertions MUST NOT appear in the `narrative` section. Ⓟ
* P02: Verification tags MUST NOT appear in indicative assertions. Ⓟ
* P03: XML and JSON forms MUST NOT embed Markdown outside the `narrative` field. Ⓟ
* P04: Metadata scalar values MUST NOT use implicit typing. Ⓟ

### Example Output (Optional)

````markdown
## Data
```yaml
version: 1.2.0
status: draft
````

## Narrative

This document defines the structure of a technical document.
Indicative statements describe what *is*.
Normative statements describe what *ought to be*.

## Assertions

* I01: A techdoc contains three sections.
* N01: A techdoc MUST preserve the order of assertions. Ⓟ

```

### Verification

**Ⓟ Provable items**  
* Section existence and ordering  
* Presence/absence of YAML block  
* Assertion structure and tag usage  
* XML/JSON shape conformance  

**Ⓗ Heuristically Acceptable items**  
* Narrative content classification  
* Semantic correctness of indicative vs normative distinctions  
* Judgment of losslessness in round-trip conversions  

**Ⓣ Testable items**  
N/A

**Ⓔ Evaluatable items**  
N/A

