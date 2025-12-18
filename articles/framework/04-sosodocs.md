<!-- markdownlint-disable MD041 -->
## 4. What is the new good enough?

We can take ideas from history and form more formal methodologies to give documents more of the precision of code without losing the human-language benefits of using an LLM.

We need to be able to give a coding AI the content a human would normally interpolate or “just know.” Once that is done, the AI behaves more like a compiler: it (unironically) transforms the input documents according to the given specifications, resolving decidable statements while passing along those that can’t be resolved.

This framing isn’t arbitrary. Source code is itself a specification. A compiler doesn’t “follow instructions”; it looks at what must be true after compilation and emits a program that satisfies that truth. This dual code versus specification view, sometimes described as proscriptive versus descriptive, or imperative versus declarative, is explored in depth in [more here](http://something.com/something), but the essential idea for us is that the high-level properties that make code compilable are the same properties that make documentation usable by a coding AI.

For brevity, we’ll start with determinism: that each statement must have one stable interpretation, and its close relative, decidability: that statements must be testable, provable, or at least checkable. Compilers rely on these constraints, and so do coding AIs. Without them, compilers fail, humans guess, and AIs hallucinate.

From this, we can derive some practical criteria for “good enough” documentation. Terms and boundaries must be explicit; vague modifiers should collapse to measurable conditions. Definitions need to be clear and unambiguous so that their meaning is fixed and names don’t drift. Functional content should appear in structured form, like enumerations or tables, so the model can treat them as resolvable units rather than prose to be inferred. Lastly, obsolete requirements or unused definitions must be removed to reduce ambiguity, which we refer to as context hygiene.

With these properties in place, documentation stops being commentary and more closely resembles a partially executable input: something both humans and AI tools can use, verify, and extend within a shared workflow.

This shift toward specifications creates a need for a systematic document structure: a small set of components that make the input resolvable, testable, and stable. We need a practical taxonomy makes maintaining discipline tractable and cheap. To make that concrete, we’ve drafted a set of modular technical documents, mostly specifications ([available here](https://github.com/your-repo/specs)), which we’ll discuss in the next section.