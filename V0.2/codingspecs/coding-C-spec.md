<!-- markdownlint-disable MD041 -->
## coding-C.spec.md: Coding Constraints for C

### Summary

This document defines the requirements and constraints for writing standalone C code targeting C99/C11 standards that emphasize readability, maintainability, portability, and safe memory management practices.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Verification Tags Vocabulary](verification-tags.vocab.md)
* [TECHDOC Structural Specification](techdoc-core.spec.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Constraints

* C01 Code MUST be compatible with C99 or C11 standards. Ⓟ
* C02 Code MUST compile with all warnings enabled and treat warnings as errors. Ⓟ
* C04 Code MUST document assumptions, limitations, and maintenance notes.  Ⓗ
* C05 Code MUST suvive static analysis tools (e.g., `clang-tidy`, `cppcheck`). Ⓗ

### Functional Constraints

* C10 Variables and functions MUST use descriptive lowercase names with underscores (e.g., `max_value`, `compute_sum`). Ⓟ
* C11 Constants and macros MUST use all caps (e.g., `MAX_SIZE`). Ⓟ
* C12 Code MUST use consistent indentation (4 spaces, no tabs). Ⓟ
* C14 Code MUST always use braces `{}` even for single-statement conditionals or loops. Ⓟ
* C15 Line length SHOULD be kept under 80 characters. Ⓟ
* C31 Code MUST define function prototypes before use. Ⓟ
* C32 Code MUST verify function return values; never ignore them. Ⓟ
* C33 Code SHOULD avoid global variables; pass parameters explicitly. Ⓟ
* C34 Functions SHOULD avoid return via parameters. Ⓗ
* C40 Code SHOULD use `else if` instead of nested `if` when possible. Ⓗ
* C41 Code SHOULD avoid `goto`, except for error handling to a single cleanup point. Ⓟ
* C60 Code MUST use `size_t` for sizes and array indexing. Ⓟ
* C61 Code SHOULD use `enum` and `typedef` to clarify intent. Ⓗ
* C62 Code SHOULD use fixed-width integer types (`uint32_t`, `int16_t`, etc.) Ⓗ
* C63 Code MUST avoid implicit type conversions that may cause truncation or overflow. Ⓟ
* C82 Headers MUST be protected with `#ifndef/#define/#endif` guards. Ⓟ

### Prohibited Elements

* C100 Code MUST NOT use deprecated C features. Ⓟ
* C101 Code MUST NOT rely on compiler-specific extensions. Ⓟ
* C102 Code MUST NOT use undefined behavior, even if it is know how the compiler handles it. Ⓟ

