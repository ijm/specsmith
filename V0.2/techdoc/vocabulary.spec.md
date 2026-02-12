<!-- markdownlint-disable MD041 -->
## vocabulary.spec: Vocabulary Specification

### Summary

A vocabulary document's sole function is to introduce and fix the meaning of DEFINED-TERMS. DEFINED-TERMS are indicated using capitalization, following established defined-term practice in legal drafting and technical standards (e.g. BCP-14) to fix meaning.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Document Vocabulary](document.vocab.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Structural Constraints

* D01 A DEFINED-TERM MUST NOT contain any unicode lowercase characters. Ⓟ
* D02 A DEFINED-TERM MUST NOT contain whitespace. Ⓟ
* A Vocabulary document:
  * V01 SHOULD NOT contain NORMATIVE STATEMENTS. Ⓗ
  * V02 MUST NOT define ADMISSIBILITY conditions for artifacts. Ⓟ
* If document B inherits vocabulary document A:
  * V03 All DEFINED-TERMS in A are in scope in B. Ⓟ
  * V04 B MUST NOT alter or redefine DEFINED-TERMS from A. Ⓟ
* D03 Capitalization within the QUOTED-PHRASE MUST NOT introduce new DEFINED-TERMS. Ⓟ
