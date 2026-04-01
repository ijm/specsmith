---
audience: Technical writers and developers who want to understand how to 'spec code'
author: Ian McEwan
copyright: (c) 2025 I.J. McEwan.
docname: Framework
license: CC BY-NC-ND 4.0
lifetime: Project
revision: 0.1.0
scope: This is a pre-publication draft article exploring a framework for writing specifications.
status: pre-publication
title: The Equilibrium Has Shifted
bibliography: references.bib
---
<!-- markdownlint-disable MD041 -->
## 1. Introduction

The existence of AI tools has caused a jump in the ever-shifting speed-rigor equilibrium we all use to evaluate projects, and our intuition needs to follow that jump. In this article we'll argue that the purpose of project documentation has subtly changed; it is no longer just a tedious overhead, but a bottleneck in the primary way to communicate with modern tools.

We'll not be concerned with AI systems whose primary value lies in open-ended conversation, creativity, or social participation. We'll focus on what we'll call *coding* agents: agents that are part of a technical workflow or build infrastructure. These systems operate entirely on authoritative inputs, typically written documents, and succeed or fail based on the precision and completeness of those inputs.

Every project lives on a spectrum between speed and rigor. At one extreme are quick fixes, MVPs, and "just ship it" decisions; at the other are detailed specifications, formal processes, and exhaustive documentation. Historically, most projects rationally leaned toward speed, accepting technical debt and relying on humans to fill in missing information. Tacit knowledge, shared experience, and 'obvious' unspoken assumptions allow teams to operate effectively with informal or incomplete documentation. Often this is a useful feature rather than a flaw, especially if the cost can be easily absorbed.

New LLM based AI tools break this system. Unlike humans, they have no social intuition, and no memory of hallway conversations. They only know what they were trained on and what's written in their context. Which means many of the disciplinary slips we've always relied on, like putting off documentation and letting knowledge live in people's heads, are no longer worth the vig.

In the following sections we'll explore specifically what coding agents need in tech documents, suggest some structure, and note some immediately useful implications. Let's start with a deeper look at the historical balance.
