<!-- markdownlint-disable MD041 -->
## coding-python.spec.md: Coding Constraints for Python

### Summary

This document defines the requirements and constraints for writing standalone Python targeting Python 3.12 that adhere to the PEP 8 style guide, use modern typing features, and follow standard conventions for command-line tools.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Verification Tags Vocabulary](verification-tags.vocab.md)
* [TECHDOC Structural Specification](techdoc-core.spec.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Constraints

* (PY01) Scripts MUST be compatible with Python version 3.12 or greater. Ⓟ
* (PY02) Scripts MUST declare UTF-8 encoding. Ⓟ
* (PY03) Scripts MUST use type hints for all function definitions and variables. Ⓟ
* (PY04) Scripts MUST conform to PEP 8 style guidelines. Ⓟ
* (PY05) Scripts MAY use features from Python 3.12 and later, including structural pattern matching. Ⓗ
* (PY06) If command-line arguments are required, the script MUST use the `argparse` module. Ⓟ
* (PY07) If the script defines an entry point, it MUST use a `main()` function with entry guarded by `if __name__ == "__main__":`. Ⓟ
* (PY08) Scripts SHOULD include a docstring at the module level describing the purpose and usage. Ⓗ
* (PY12) Type annotations MUST use standard Python `typing` or built-in generic syntax (e.g. `list[str]`, `dict[str, int]`). Ⓟ
* (PY13) Scripts MUST NOT use wildcard imports. Ⓟ
* (PY14) Functions and variables SHOULD use `lowercase_with_underscores` naming. Ⓗ
* (PY15) Classes SHOULD use `CapitalizedWords` naming. Ⓗ

### Prohibited Elements

* (PY21) Scripts MUST NOT use deprecated Python 3.12+ features. Ⓟ
* (PY22) Scripts MUST NOT rely on features that are only available in Python 3.13 or later. Ⓟ
* (PY23) Scripts MUST NOT use non-standard libraries without explicit declaration. Ⓟ
* (PY24) Scripts MUST NOT contain top-level executable code aside from guarded `main()` calls. Ⓟ
