<!-- markdownlint-disable MD041 -->
## Fast or Easy versus Slow or Correct

So, do you cut corners to get something running today, or do you take the time to build it properly so you won’t pay for it later? Modern tools that can seemingly build entire applications from a single sentence have only exacerbated this abiding tension.

The financial world has a neat framing for this tradeoff in *net present value*. A shortcut pays off immediately, while the costs of technical debt, that is, rewriting or re-architecting later, along with the opportunity cost of not building something else are discounted into the future. If the shortcut gets you a customer demo, a market lead, or simply lets your team ship this quarter, the math looks obvious: do it fast, fix it later.

This logic shaped entire eras of software and product development from the 1980s through the dot-com boom with the *Worse is better* motto (ref). The *MVP* (minimum viable product) and *Vertical Slice* goals are still common today (refs). "*Adequate now* is worth more than *perfect someday*" is a common refrain because it is genuinely true that even if an entire system has to be thrown away and rebuilt, an early advantage often more than justified it.

But it does have a dark side. Incentive structures often reward speed over quality, engendering a culture of hot-fixes that is self-perpetuating as the project spirals with hunts for fast fixes to problems caused by fast fixes; borrowing from peter to pay paul. Sub-projects are often treated as self-contained and incorrectly apply this balance while ignoring a larger context that could easily support a more thoughtful approach. The desire for faster-better-cheaper is always present and pushed for, but those doing the pushing often lack precisely the knowledge needed to evaluate the future costs properly, or they know that they will not be the ones paying the bill when it comes due. Projects get a feeling of 'fast and loose' and never doing anything properly even when there is time available.

The straw man at the other extreme of rigorousness involves formal requirements, specifications, and communications. Every decision or discussion requires scheduled meetings before its inclusion in carefully maintained, forensically traceable documentation. This was reserved for environments where mistakes can be catastrophic like aerospace, finance, safety systems, etc. The associated infrastructure is complex and expensive. It also has it's own bugs, so even with all that, disasters still happen (refs). This heavy weight is rarely liked, and project discipline feels more like a method of butt covering and divesting blame rather than a true commitment to quality.

For most situations, fast iteration and informal knowledge transfer look like they kept projects moving. New and old hires absorb or create institutional knowledge by trial and error.  This isn't sloppiness, its good tactics: "Why do we need to write everything down? We all know it. Just write down the important things, we need to be moving!".

It is the reliance on human communication, memory, and cooperation that distinguishes these two cultural extremes. Between them there is a rational equilibrium, a perfect strategy. One which is constantly battled over, but ironically, rarely thought or reasoned about more formally.

LLMs and other AIs do not participate in any culture, they do not learn like newcomers, and have no way to discover common knowledge.  This is the new problem we need to address.
