---
title: Specifications as Theories, A Constraint-Invariant View of Technical Documents
docname: DeepTheory
scope: This is an abstract foundational theory document.
audience: Highly technical or mathematically inclined devs who want to understand the theory behind the broader industry of specification provers and how that interacts with the Techdoc framework.
author: Ian McEwan
license: CC by-nc-nd 4.0 
lifetime: Project
revision: 0.1.0
status: pre-publication
copyright: (c) 2025 I.J. McEwan.
---
## 1. Introduction

A rigorously written specification can be understood as a formal theory whose admissible implementations are models, whose verification mechanisms are proof systems, and whose encodings are structure-preserving representations. When specifications are constructed from explicit definitions (INDICATIVE statements in our framework), constraints (NORMATIVE statements in our framework), and declared verification methods, meaning becomes the set of invariants preserved across admissible transformations rather than any particular representation. This view unifies specification authoring, tooling, formal reasoning, and specifically improves LLM consumption under a single semantic framework.

## 2. Specification Structure as Theory Presentation

A well-structured specification naturally decomposes into elements analogous to logical theory components.

### INDICATIVE Statements are Vocabulary and Definitions

Indicative Statements ("What is") fix meaning. They define terms, domains, and interpretation rules. In logical terms, they correspond to signature definitions and semantic groundings.

### NORMATIVE Statements are Constraints and Axioms

Normative statements ("What ought to be") restrict the admissible realizations and define the space of valid artifacts.

### Verification Annotations are Proof Obligations and Evidence Classes

These describe how conformance can be established without altering meaning and correspond to proof strategies, decision procedures, or evidence classes.

Under this mapping, a specification becomes a theory presentation, that is, a set of definitions and constraints that determine a space of admissible models.

## 3. Implementations and Artifacts as Models

Any artifact that satisfies all normative constraints is a model of the specification. This applies uniformly across domains such as Software systems, Documents, Electronic circuits, and Protocol realizations.

In model theory terms, we can define a specification's meaning as the set of all admissible models, and implementations as witnesses that this set is non-empty. This is because the specification does not describe how to construct artifacts, only which artifacts are admissible.

## 4. Encodings as Structure-Preserving Representations

If multiple translations exist (e.g., XML, Markdown, logical form, other human languages), they should preserve meaning through reversible transformation and no encoding is privileged.

If this is strongly enforced then 'Meaning' becomes what survives all admissible transformations. Each encoding is a projection of the same invariant structure.

The abstract specification is therefore not a "master encoding" but the equivalence class of all admissible encodings under lossless transformation.

While we can enforce this under format changes, it is harder to do across human languages, or when encoding for a theorem prover. However the idea remains sound.

## 5. Verification as Proof or Model Checking

Verification methods correspond to proof classes:

  Verification Type     Logical Analogue
  --------------------- -----------------------------------------
  Static provability    Formal proof / decidable property
  Testability           Model execution / counterexample search
  Evaluatable metrics   Quantitative constraint satisfaction
  Heuristic review      Probabilistic or human proof search

Verification does not add meaning. It establishes evidence that a model satisfies the theory.

## 6. Procedural Meaning via Invariance

Traditional specifications often define meaning declaratively ("this text means X"). A constraint-invariant specification instead defines meaning operationally: Meaning is all information that cannot be changed by admissible transformations.

Transformations may re-encode, normalize, assemble context, or remove explicitly superseded rules, but they can (must) not introduce new constraints, infer unstated meaning, or alter normative strength or forcefulness.

This produces a semantics based on invariants rather than representation. This view aligns with representation-independent approaches in formal methods, but is motivated by modern toolchains and LLM-based language processors.

## 7. Advantages and Implications

This method has useful advantages:

* Encoding Independence: Meaning is preserved across formats and translations without canonicalization.
* Composition Safety: Context assembly becomes normalization with no override reasoning.
* Toolchain Robustness: Build steps cannot silently alter semantics if admissibility is enforced.
* Formal Reasoning Compatibility: The same specification can be mapped into formal logic, SMT constraints, or proof assistant representations without needing to be semantically reinterpreted.

And useful implications:

* Specifications become executable semantic objects. They can drive code generation, verification tooling, and automated reasoning from the same source.
* Implementations become model construction and engineering becomes constrained model building.
* Encodings become interchangeable views with different formats optimize for authoring, transport, reasoning, or tooling.
* Verification becomes evidence production and not a reinterpretation of requirements.

## 8. Conceptual Summary

A rigorously constrained specification ecosystem naturally forms a semantic stack, where specifications become theories, implementations become models, verifications generate evidence, encodings become structure-preserving representations, and assembly becomes theory normalization.

In this framework, meaning is not tied to the text itself or tooling but is the invariant structure defined by the text's definitions and constraints. The text ceases to be a purely descriptive document and instead becomes a formal semantic system. This enables a unified pipeline where reasoning, automated tooling, and more formal methods can operate over the same artifact without reinterpretation.

The result is a specification ecosystem where semantic drift is not just discouraged but structurally disallowed.
