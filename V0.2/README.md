# TECHDOC

TECHDOC is a framework for writing technical specifications in **ordinary technical English** such that they can be *unambiguously understood, ingested by tools, and used to assess admissibility of artifacts*, without forcing authors to abandon established best practices or rewrite documents in a formal language.

The goal is to introduce a *minimal* set of structural and linguistic conventions that let a specification say both what is allowed or required, and how conformance to those requirements can be evaluated.

These can be summaries as : Use standard technical english, legal contract like capitalized terms, ladled bullet lists, and try to separate narrative, assertive, and imperative sections.

## Why TECHDOC

In most specification workflows a specification describes what to build, while separate documents, tools, or interpretations are needed to describe how to test or validate it.

Over time, these diverge.

TECHDOC is designed so that:

* The specification itself defines admissibility.
* Verification criteria are not added later or inferred informally.
* Tools can be built directly from the spec to check whether an artifact conforms.

The same document that constrains artifacts also constrains how conformance is demonstrated.

## Description

The Frame work lets you write specifications using familiar conventions like standard technical english or capitalized defined terms.

TECHDOCS Clearly separate narrative explanations, assertive definitions, or imperative instructions. They state not only *what* is required, but *how* conformance may be evaluated.

## Admissibility and Verification

In TECHDOC:

* normative assertions define constraints on admissible artifacts.
* Verification indicators hint how those constraints may be evaluated.
* A verification encoding makes the evaluative structure explicit.

From a single specification, it is possible to derive:

* admissibility criteria for artifacts, and
* procedures or checks that establish whether those criteria are met.

The specification remains the source of truth; verification artifacts are derived from it.

## What TECHDOC Does *Not* Require

* No formal logic authoring
* No canonical encoding
* No schema-first workflow
* No separate “test specification” document

Natural language remains the primary authoring surface, and formal representations are optional, derived views.

## Core Ideas

TECHDOC works by placing strict but minimal constraints on:

* how terms are defined and scoped
* where normative meaning is allowed to appear
* how assertions are identified and ordered
* how verification intent is expressed

## Repository Contents

This repository contains:

* **Core specifications**

  * document structure
  * vocabulary and defined-term rules
  * separation of narrative, indicative, and normative content
* **Encoding profiles**

  * Markdown
  * JSON
  * XML
* **Verification vocabulary and encoding**

  * standardized verification indicators
  * an abstract encoding of evaluative structure
* **Tools** (where present)

  * parsers and linters
  * encoding converters
  * admissibility-checking and verification tooling

## Intended Audience

TECHDOC is for people who write, maintain, or consume technical specifications and need those specifications to:

* remain readable and writable as documents
* precisely constrain admissible artifacts
* support verification without reinterpretation

It assumes familiarity with specification-style writing.

## Current Status

This is an evolving project. The focus is on semantic clarity, round-trip stability, and practical use, rather than formal maximalism or completeness.
