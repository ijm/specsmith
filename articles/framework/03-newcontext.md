<!-- markdownlint-disable MD041 -->
## 3. The Machine Can’t Read the Room

Unlike humans, LLM based AI tools can't patch gaps through lunch time discussions, a glance at half-written notes, or an overheard hallway comment. They lack the back-channels humans unconsciously rely on. Everything an LLM can know must be stored in its trained neuron weights, which are highly abstracted difficult to interpret functions, or in the text of its immediate working context, which suffers from all the laxness problems of human language.

If crucial information is in neither place then it simply doesn’t exist, and whatever is missing must be extrapolated to form a best guess, often in the form of a hallucination.

Worse, conversational corrections, now common in many applications, often make things unstable. The LLM can see both the mistake and the correction and will often revert to the wrong one, especially if the error fits its internal training bias. What a human would internalize as a “lesson learned,” an LLM sees as more of an interesting suggestion for a temporary correction. To actually internalize it, the LLM must be re-tuned, with all the time and cost that entails.

For these tools to produce good results, and especially for coding AIs, we must give them the right information, and only the right information. It's garbage in, garbage out.

However, the same is true for newly hired humans. If you give them vague specs, missing assumptions, an obscure tribal shorthand, and then fail to answer their questions or provide any feedback, then the new hire will produce slop. Switch to another new hire and they’ll produce a variation of the same slop. That is, remove the back channels and similar slop-inducing pathologies arise in humans, unless you are very lucky.

This “luck” leads to a second anti-pattern: keep hitting that enticing redo button and hope for a “good-enough” jackpot. It’s a classic human behavior that taps into our gaming or gambling reflex; think school sci-tech expos, hackathons, or game jams, where a few “winners” emerge from a pile of under-specified but enthusiastic slop. Only now, with an AI, we can indulge this pattern dozens of times in minutes, and without HR inquiring about new hire or intern mistreatment.

Success stories for generative AI generally fall into two categories: amazing results from almost no information, or good results when given clear rules, instructions, and goals. The former is the “luck” or “vibe” pattern. The latter has spawned “prompt engineering” and “specification coding”. The formality implied by these latter names and the frequent recommended use of “plain language principles” or “simplified technical English” is what this article explores.

The thesis here, then, is that “slop” isn’t a problem with coding AIs per se, but an externalization of the lack of access to the back channels and common knowledge that keep human productivity functional. Without enshrining this informal tacit common knowledge into something a coding AI can ingest, its effectiveness is down to luck at best.

The purpose of project documentation, then, has subtly shifted. It’s no longer just a message to our future selves about what was created, how to use it, and perhaps some forensics about decisions along the way. It is now an active part of the forward-looking engineering, and includes sufficient information for any human or coding AI to recreate the work in isolation.

By *active* I mean that it must be kept up to date, is part of, and plays a continuous role in, the engineering build process. It is never just a historical starting point that gets left behind, but a current source of information. In a software project, we’d call that “source code.”

This is why we call them *coding* AIs: they treat all documentation the way a compiler, linter, or debugger treats source code.

The idea of documentation as code, or specification as code, isn’t new; it’s been around for decades. But this is a new twist, with new rules, new tricks, and new shortcuts. Coding AIs now allow us to “compile” documentation into other artifacts like code, tests, evaluations, or other documentation.
