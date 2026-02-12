<!-- markdownlint-disable MD041 -->
## std.vocab: Standard Vocabulary

### Summary

This document introduces DEFINED-TERMS used across the TECHDOC framework.

### Inheritance

#### Inherits

* [Vocabulary Specification](vocabulary.spec.md)

### General Definitions

* D01 A TECHDOC is a document conforming to the [TECHDOC Specification](techdoc.spec.md) in this framework.
* D02 An artifact is ADMISSIBLE if it satisfies all constraints in its governing document.

### Normative INDICATORS

* D11 MUST implies an unconditional constraint.
* D12 SHOULD implies a recommended constraint whose violation requires justification.
* D13 MAY implies an optional behavior.
* D14 NOT is a negation operator that inverts the constraint.
* D15 MUST NOT implies a prohibited behavior or state.
* D16 SHOULD NOT implies a discouraged behavior whose use requires justification.

### Defining terms and phrases

* D21 A DEFINED-TERM is a capitalized lexical unit, consisting of a single word or multiple words joined by hyphenation, whose meaning is fixed by exactly one defining INDICATIVE STATEMENT. It is a lexically disciplined word.
* D22 A QUOTED-PHRASE is defined by quoting the phrase, with any quotation marks, in an INDICATIVE statement.
* D23 An INDICATOR is a word or symbol whose presence denotes that the associated statement is to be interpreted according to a specific DEFINED-TERM or semantic classification.

Additional constraints on interpretation:

* D31 A DEFINED-TERM MAY be pluralized and MAY act as a symbolic definition.
* D32 Multi-word capitalization without hyphenation MUST NOT be interpreted as a DEFINED-TERM. Whitespace indicates they are separate words.
* D33 A reader or processor MUST NOT introduce, assume, or invent DEFINED-TERMs beyond those explicitly defined in in-scope documents.
* D34 A QUOTED-PHRASE SHOULD NOT be interpreted as introducing a new DEFINED-TERM.
* D35 Uncapitalized or unquoted words or phrases MAY be defined by INDICATIVE statements to clarify colloquial meaning.
* D36 Uncapitalized forms SHOULD be interpreted as ordinary language without carrying additional normative force.
