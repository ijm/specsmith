<!-- markdownlint-disable MD041 -->
## What is the new good enough?

First, what properties or attributes do we want from our AI tools? If we accept that 'documentation' (in the form of prompts, specs, etc) is the way we get an AI to correctly do our bidding, then what structure, or properties do we need to impose on those documents to get those desired properties or attributes from the AIs?

This question can obviously go in many directions, but the properties I want to focus on are:

* Determinism: A given input always produces the same output, up to some acceptable variability, and
* Decidability: There is some way, from the output, to prove or test that the input was adhered to.

With these two properties we can iterate and evaluate the output of an AI tool.

This make our question wonderfully meta: We're asking what structure is 'good enough' in our instructions, so that we can evaluate that the output of the tool is good enough for whatever it is we want *that* to do.

Determinism and decidability are properties we expect of code or a well written procedure. When we apply these ideas to documents we often call them 'specifications'.

However we can always think of code as a specification, or a specifications as code. Code and specifications are two sides of the same coin, and there is a deep connection and duality between them that we'll explore in depth in this (ref) article. For now, we only need a simple view of how they are related.

Code tells you how to do something, while a specification tells you what is true about something.

We'll use a toy example involving 'C' code, but this applies to any procedure or activity. So:

```C
int X = a + b;
int Y = a + b;
```

You probably read this as "add `a` to `b` and put it in `X`, then add `a` to `b` and put it in `Y`". Which we'll call the procedural or code view of the code. You'd also expect a compiler to optimize the obvious redundancy here. It can do that because this isn't a procedure, but a specification: "The variable `X` must contain the sum of `a` and `b`. The variable `Y` must contain thee sum of `a` and `b`". As long as `X` and `Y` come out that way, we don't care how the compiler gets there. This is the specification view of the same code.

If we give chatgpt or Claude the prompt:

```text

Generate the C statement lines that meet the following specifications:

* the integer X must contain the sum of a and b.
* the integer Y must contain the sum of a and b.

Output only the code. Do not explain or comment.
```

It outputs exactly that above C code (link).

Again this can apply to any activity, for example the duality between "Go to the store and buy 3 apples and 2 bananas" and "When you (legally) leave the store you must have 3 apples and 2 bananas". So is a grocery list a specification or a procedure? And what does the checkout receipt tell you?


