## heuristics-testing-prompt-spec: Heuristic Verification Prompt Specification

### Summary

Defines how to construct prompts that enable human or AI evaluation of Ⓗ-tagged heuristic requirements in a specification. Given a target specification with Ⓗ items, this meta-specification generates a prompt that can validate the output of that specification by applying heuristic judgment.

### Scope and Intent

This specification is used to create *evaluation prompts* that apply to the output of a given specification. The output prompt MUST ask the model or human reviewer to check heuristic qualities defined in the original specification, including style, clarity, consistency, and subjective readability.

### Metadata

```yaml
version: 1.0.0
```

### Imports and Inheritance

* This specification conforms to the Commonmark Markdown specification.
* This specification conforms to the BCP 14 keyword specification.
* The tag symbols Ⓟ, Ⓣ, Ⓔ, and Ⓗ definition and usage conform to the verification-tags-spec specification.
* The Metadata section conforms to the metadata-spec specification.

### Terminology and Conventions

The key words "MUST", "MUST NOT", "SHOULD", etc., follow BCP 14 semantics.
The term **target specification** refers to the document being validated.
The **evaluation prompt** is the output of this specification — a prompt that asks for heuristic assessment of an output derived from the target specification.

### Functional Requirements

* The testing prompt specification MUST extract all Ⓗ-tagged requirements from the target specification. Ⓟ
* For each Ⓗ item, the generated evaluation prompt MUST include a concise question or instruction that checks the intent of that requirement. Ⓟ
* The evaluation prompt MUST explicitly refer to the output to be evaluated, e.g., "the generated code" or "the specification produced". Ⓟ
* The evaluation prompt SHOULD ask for justification, explanation, or examples of failure where relevant. Ⓗ
* The evaluation prompt MUST produce a grade each item on a scale of (A-D, F). Where A indicates excelence, C is a passing grade, and F indicates complete failure or non-compliance.
* If no Ⓗ-tagged items exist in the target spec, the evaluation prompt MUST indicate that no heuristic verification is applicable. Ⓟ
* The final evaluation prompt MUST be framed as a task that can be used in a chat or prompt-engine context (i.e., natural language, concise, and self-contained). Ⓗ

### Structural Constraints

* The generated prompt MUST be in natural language suitable for use in a prompt to an LLM. Ⓟ
* Each heuristic requirement SHOULD become a bullet point in the evaluation prompt unless combining them improves clarity. Ⓗ
* Each bullet MUST trace back to the original requirement, directly or paraphrased. Ⓟ

### Example Output (Optional)

**Example Evaluation Prompt for a Spec with Heuristic Requirements:**

> Please review the generated specification and assess the following heuristic qualities:
>
> * Is the language clear, direct, and free of ambiguity?
> * Does the document use imperative voice consistently?
> * Are section headers used and formatted in a human-readable, unambiguous way?
> * Does the document formatting promote readability and clarity for a junior developer?
>
> For each item, explain any failures or weaknesses. If all criteria are met, state that explicitly.

---

You can now feed this **`heuristics-testing-prompt-spec`** and a **spec-to-build-test-for** into an LLM and ask:

> Use the `heuristics-testing-prompt-spec` on the `spec-to-build-test-for` to build a prompt that can be used on what the `spec-to-build-test-for` would produce to validate it.

This will yield a prompt tailored to the Ⓗ rules in the target spec.

