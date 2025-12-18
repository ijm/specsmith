<!-- markdownlint-disable MD041 -->
## 5. Toward a Taxonomy for Human-/AI-Readable Technical Documents

Our practical aim now is to create documents that can be

* checked by a non-technical stakeholder to confirm intent,
* used by a developer (human or AI) to generate an artifact, and
* used by a tester (human or AI) to verify that artifact.

A single *source* of truth for all stages of development and verification that also follows the philosophy of section 4.

This allows coding AIs to participate in the iterative loop we already use: build something, verify it, inspect the failures, refine things, rinse, and repeat. The errors in each loop shrink, and a consistent desirable result emerges. Making this stable and predictable for an LLM clarified how the components of each document influence model behavior and informed the taxonomy choices for our documents. We go into depth about this approach [in this article](http://localhost/otherarticle), but here we focus on the high-level principle of determinism and decidability.

Technical documents and source code are expressions of the same idea: a description of what is or must be true about some objective entity. Using this lens, we can borrow familiar compiler workflow concepts and language and apply them to how an AI should process documents, particularly in how they handle static analysis and verification.

To make this workable, we use a high-level template that separates narrative statements from assertions and splits assertions into facts (indicative “what is” statements) and constraints (normative “what ought to be” statements). This allows verifications to be explicit.

With this structure, the coding AI can treat a document the way a compiler treats source: resolve what can be deterministically decided, propagate what cannot be decided, and generate verification logic to confirm compliance.

A useful idea arose from a common failure mode familiar to many AI-generated tests: meaningless checks like asserting that `3.14159 == 3.14159`. Our fix was to attach verification hint tags on each normative statement, indicating what is statically provable, what requires execution testing, and what requires human or heuristic validation. Those tags became their own specification because they exert such strong influence on model behavior.

At this point a practical taxonomy emerges, not as rigid sections, but as a small set of components that must exist somewhere in every document:

* narrative context (why the thing exists), as narrative statements;
* definitions and terminology (the environment in which statements are interpreted), as indicative statements;
* atomic requirements with verification tags, as normative statements;
* a short list of prohibited or ambiguous constructions;
* optional examples that act as additional constraints.

Again, this isn’t bureaucratic layering. Templates give predictable defaults, reduce friction, and remove accidental ambiguity, lowering cost while allowing both humans and coding AIs to reliably transform documents, even when unaware they are doing so.

Over time, this pushes toward a more interesting outcome: documents become partially executable specifications. They don’t merely describe systems; they participate in building them—generating code, tests, evaluations, and downstream artifacts. As tools mature, writing such documents becomes a form of programming at a higher level of abstraction, much as C is to assembly.
