<!-- markdownlint-disable MD041 -->
## Vocabulary Specification

### Summary

A vocabulary document's sole function is to introduce and fix the meaning of DEFINED-TERMS. DEFINED-TERMS are indicated using capitalization, following established defined-term practice in legal drafting and technical standards (e.g. BCP-14) to fix meaning.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Document Vocabulary](document.vocab.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Definitions

* D01 A DEFINED-TERM is a capitalized lexical unit whose meaning is fixed by exactly one defining INDICATIVE STATEMENT.

### Structural Constraints

* D02 A DEFINED-TERM MUST NOT contain any unicode lowercase characters.
* D03 A DEFINED-TERM MAY consist of a single word or of multiple words joined by hyphenation.
* D04 A DEFINED-TERM MUST NOT contain whitespace.
* D05 Multi-word capitalization without hyphenation MUST NOT be interpreted as a DEFINED-TERM.
* A Vocabulary document:
  * V01 MUST NOT contain NORMATIVE STATEMENTS.
  * V02 MUST NOT define ADMISSIBILITY conditions for artifacts.
* If document B inherits vocabulary document A:
  * V11 All DEFINED-TERMS in A are in scope in B.
  * V12 B MUST NOT alter or redefine DEFINED-TERMS from A.
