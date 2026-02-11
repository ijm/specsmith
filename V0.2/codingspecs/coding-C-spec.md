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
* C03 Code MUST avoid global variables; pass parameters explicitly. Ⓟ
* C04 Code MUST document assumptions, limitations, and maintenance notes. Ⓗ

### Naming and Formatting Constraints

* C10 Variables and functions MUST use descriptive lowercase names with underscores (e.g., `max_value`, `compute_sum`). Ⓟ
* C11 Constants and macros MUST use all caps (e.g., `MAX_SIZE`). Ⓟ
* C12 Code MUST use consistent indentation (4 spaces, no tabs). Ⓟ
* C14 Code MUST always use braces `{}` even for single-statement conditionals or loops. Ⓟ
* C15 Line length SHOULD be kept under 80 characters. Ⓟ

### Function Constraints

* C31 Code MUST avoid global variables; pass parameters explicitly. Ⓟ
* C32 Code MUST define function prototypes before use. Ⓟ
* C33 Functions SHOULD avoid return via parameters. Ⓗ
* C34 Code MUST verify function return values; never ignore them. Ⓟ

### Control Flow Constraints

* C40 Code SHOULD use `else if` instead of nested `if` when possible. Ⓗ
* C41 Code SHOULD avoid `goto`, except for error handling to a single cleanup point. Ⓟ
* C42 Code MUST avoid magic numbers; define named constants. Ⓟ

### Data and Type Constraints

* C60 Code MUST use `size_t` for sizes and array indexing. Ⓟ
* C61 Code SHOULD use `enum` and `typedef` to clarify intent. Ⓗ
* C62 Code SHOULD prefer fixed-width integer types (`uint32_t`, `int16_t`, etc.) Ⓗ
* C63 Code MUST avoid implicit type conversions that may cause truncation or overflow. Ⓟ

### Error Handling Constraints

* C70 Code MUST handle all error conditions gracefully and explicitly. Ⓟ
* C71 Code SHOULD use consistent error codes or return conventions. Ⓗ
* C73 Code MUST fail safely with predictable behavior even on error. Ⓟ

### File Organization Constraints

* C80 Code MUST be split into `.h` headers and `.c` source files. Ⓟ
* C81 Headers MUST contain only declarations and `#define`s — no variable definitions. Ⓟ
* C82 Headers MUST be protected with `#ifndef/#define/#endif` guards. Ⓟ

### Testing and Analysis Constraints

* C90 Code MUST run static analysis tools (e.g., `clang-tidy`, `cppcheck`). Ⓟ

### Prohibited Elements

* C100 Code MUST NOT use deprecated C features. Ⓟ
* C101 Code MUST NOT rely on compiler-specific extensions. Ⓟ
