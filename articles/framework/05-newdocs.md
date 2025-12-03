## 5. Toward a Taxonomy for Human-/AI-Readable Technical Documents

Moving to more practical matters, we've drafted a set of modular specifications and technical documents (available on [github](https://github.com/your-repo/specs)) that follow the above philosophy in the mold of standard documentation libraries.

The original goal was simple: a human and AI readable document that can :

* be used by someone (non-technical) to confirm that it encapsulates what is desired (for example a customer or stakeholder);
* be used by a developer (human, AI, or machine) to generate an artifact (for example, a code module, or another specification)
* be used by a tester (human, AI, or machine) to verify the artifact is what is wanted (for example, proofs, test code, or a QA procedure)

That is the document is a single *source* of truth for all stages of development and verification.

This allows AIs to participate in the powerful loop we already do naturally, where we use feedback from the results of building, linting or otherwise testing an artifact, to refine things and loop again. Rinse and repeat until we hopefully arrive at a consistent desirable result.

This informed the taxonomy choices for our documents and forced a sharper understanding of how the components of each document influence the LLM. We go into much more depth about this approach [in this article](http://localhost/otherarticle), but below focus the top-level principle of determinism and decidability following from section 4.

So, in section 4 we argued that technical documents and source code are different expressions of the same idea, both are a description of what is or must be true about some objective thing. Using this idea we can steal some familiar compiler workflow concepts and language, and apply them directly to how an AI should handle documents, particularly in how they process static analysis and verification.

First we want a general high-level template for our documents that follows good technical writing practices. We'll separate narrative statements from assertions, and then split assertions into facts (indicative statements - things that are true now) and constraints (normative statements - things which ought to be true). This will also let us make verifications explicit wherever possible.

With this separation in place, the AI can treat a document the way a compiler treats source: resolve what can be decided immediately, propagate what cannot, and generate verification logic to confirm that the constructed object satisfies the specification.

An interesting innovation came about from a common failure mode familiar to many AI-generated tests: meaningless checks like asserting that `3.14159 == 3.14159`. Our fix was to attach verification hint tags on each normative statement, indicating what is statically provable, what requires execution testing, and what requires human or heuristic validation. Those tags became their own specification.

At this point the shape of a practical structure emerges, not as rigid sections, but as a small set of components that need to exist somewhere in every document:

* narrative context (why the thing exists);
* definitions and terminology (the environment in which statements are interpreted);
* atomic requirements with explicit verification tags;
* a short list of prohibited or ambiguous constructions;
* optional examples that act as additional constraints.

Again, none of this is about bureaucratizing writing; Templates provide recognizable common structures, which become easy to scan and provide defaults for most of the unimportant details and ideal lower the effort required to create and maintain documents. Additionally, we provide a structural framework that reduces unnecessary ambiguity so that AI tools, or a human, can reliably perform transformations on the document even if they do not realize that is what they are doing.

Looking forward, this direction points toward a more powerful process: documents evolve into partially executable specifications. Instead of being static descriptions, they are objects that participate in the build process. They can generate artifacts, tests, constraints, and even downstream documents. Over time, technical documents won’t merely guide or memorialize development but will instead become essential components in it, shaping how systems are built as directly as source code does today. As tooling and norms catch up, it may be that writing such documents will be seen as genuine coding at higher level, much as coding in C is to assembly.



