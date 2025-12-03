## 5. Toward a Taxonomy for Human-/AI-Readable Technical Documents

We've been working on [a set of modular specifications and technical documents](https://github.com/your-repo/specs) that follows the above philosophy and can be processed by AI tools. We initially focused on creating structured specifications where we could generate both the desired object (say some code module) and a set of verifications of that object from the same specification. The goal was to have the output of the verifications looped back to the generating AI to ensure the output code meets the specification in the same way that compiler errors are currently looped back to fix code issues.

Getting this to work led to a clearer understanding of how we should structure documents [explored more in this article](link), including how to use specifications to build specifications. But for the purposes of this discussion, we're arguing for a general shift in intuition, we will focus only on the top level and the initial ideas of determinism and decidability.

In section 4 we argued that technical documents and source code should be seen as different instantiations of the same idea, that is, describing what must be true about the result, so we can apply some concepts from compiling code to inform how the AI should translate documents.

First we should separate narrative or explanatory statements from normative statements, and then facts from constraints. This will let us make verifications explicit wherever possible.

We can now treat the documents more like a compiler would. The AI can separate the parts that can be resolved (decided) immediately from those that must be passed downstream into the object being constructed. It can also generate verification code to check that what was actually constructed meets the specification.

However we found that, like much AI generated test code, it would often do silly things like add a test function to check that `3.14159 == 3.14159`. We solved this by adding verification hints, or tags to each normative statement to indicate what should be, for example, provable directly from the outputted object (such as by linting), what requires some form of execution testing, and what must be validated more subjectively maybe by a human. Which we, of course, turned into a specification document.

So, a practical taxonomy has a few core components:

### Narrative Sections for Summary and Intent

These are mostly for human context. They explain what the system is for, why the spec exists, and what problem it solves. They shouldn't contribute to the executable or resultant structure directly.

### Definitions and Terminology

A glossary of terms, domain concepts, naming conventions, and the meanings of normative keywords. These eliminate ambiguity at the root. The definitions are part of the "compile-time environment" and resolve the meaning of later statements deterministically.

### Functional Requirements

These are the actual constraints and behaviors. These should be bullet-point like, with each normative statement covering a single or atomic unambiguous item, free of narrative language, and expressed in a way that can be decided or propagated, and hint (tagged) at how verification should be achieved.

That tagging system is a key shift: it tells the implementer which parts must be enforced and which parts must be carried forward to the next transformation step. Experienced attentive humans do this intuitively, but everyone (and thing) else benefits from explicit guidance.
