<!-- markdownlint-disable MD041 -->
## techdoc-encoding-xml.spec: TECHDOC XML Encoding Profile

### Summary

This document defines an XML-based ENCODING profile for TECHDOCs.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Verification Vocabulary](verification-tags.vocab.md)
* [TECHDOC Structural Specification](techdoc-core.spec.md)
* [TECHDOC Encoding Specification](techdoc-encoding.spec.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Specification

* (X01) A TECHDOC MUST be represented as a single XML document. Ⓟ
* (X02) The root element MUST be `<techdoc>`. Ⓟ
* (X03) The `<techdoc>` element MUST contain:
  * a `<title>` element containing the TECHDOC name. Ⓟ
  * an ordered sequence of `<section>` elements. Ⓟ
* (X04) Each `<section>` element MUST contain:
  * a `name` attribute whose value is the SECTION name. Ⓟ
* (X05) NARRATIVE and ASSERTION SECTIONS MUST contain:
  * an ordered sequence of `<statement>` child elements. Ⓟ
* (X06) NARRATIVE and INDICATIVE STATEMENTS MUST be encoded as `<statement>` elements containing text content only. Ⓟ
* (X07) NORMATIVE STATEMENTS MUST be encoded as `<statement>` elements with:
  * an `id` attribute containing the STATEMENT identifier, Ⓟ
  * a `type` attribute mapping to the verification INDICATOR, Ⓟ
  * text content containing the STATEMENT text. Ⓟ
* (X10) Data SECTIONS MUST contain exactly one `<data>` child element with:
  * a `language` attribute identifying the data language (e.g. `yaml`, `json`), Ⓟ
  * text content containing the serialized data. Ⓟ
* (X40) SECTION order MUST be preserved by document order. Ⓟ
* (X41) STATEMENT order MUST be preserved by element order. Ⓟ
