<!-- markdownlint-disable MD041 -->
## 3. The Machine Can’t Read the Room

Unlike humans, AIs can't patch gaps through conversation, a glance at half-written notes, or an overheard hallway comment. They lack the back-channels all human unconsciously rely on. Everything an AI can know must be stored in its trained neuron weights which are highly abstracted functions that are difficult to interpret, or in the text of its immediate working context, which suffers from all the laxness problems of human language.

If crucial information is in neither place, it simply doesn’t exist for the model. If something missing is needed then the model must make a best-guess often in the form of a hallucination.

Worse, conversational corrections, common to many current tools, often make things unstable.  The model can see both the mistake and the correction, and will often revert to the wrong one, especially if the error fits its internal training bias.  What a human would internalize as a 'Lesson learned', an LLM sees as more of a suggestion for a local correction. To internalize it the model must be re-tuned, with all the time and cost that entails.

For an AI to produce a good result it must be given the right information, and only the right information. It's garbage in, garbage out.

However the same is true for humans. If you give a new hire vague specs, missing assumptions, an obscure tribal shorthand, and then fail to answer their questions or provide any feedback they'll produce slop. Switch to another new hire and they'll produce a variation of the same slop. That is, remove the back channels and similar slop-inducing pathologies arise in humans, unless you are very lucky.

Modern AIs let you indulge this luck pattern dozens of times in minutes, and without HR inquiring about intern misuse. It taps straight into our gambling reflex: hit the enticing re-roll button, and hope for a “good-enough” jackpot. It’s classic human behavior; think school sci-tech expos, hackathons, or game jams, where a few “winners” emerge from a pile of under-specified but enthusiastic slop.

However success stories for generative AIs do not generally follow this pattern. Instead they seem to stem from being given clear rules, clear instructions, and a clear goal. There is now an entire field of prompt engineering, with many write-ups, how-tos, and even courses on how to write prompts to get effective results.

The thesis here then, is that 'slop' isn't a problem with AI per se, but an externalization of the lack of access to the background noise and common knowledge that keeps human productivity functional.  Without enshrining tacit common knowledge into something the AI can ingest, the effectiveness of AI tools is down to luck at best.

The purpose of project documentation then has subtly shifted. It's no longer just a message to our future selves about what was created, how to use it, and perhaps some forensics about decisions along the way. It now includes an active forward looking communication about how to get there, sufficient for any human or AI to recreate the work in isolation.

We have names for that kind of document: We call them procedures, programmes, or code.

The idea of documentation as code, or specification as code isn't new, it's been around for decades, but this is a new twist, with new rules, new tricks, and new shortcuts. AI tools now allow us to 'compile' documentation into other things like code, tests, evaluations, or other documentation.
