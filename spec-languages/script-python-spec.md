## script-python-spec: Python Script Specification

### Summary

This specification defines the requirements and constraints for writing standalone Python scripts targeting Python 3.10+ that adhere to the PEP 8 style guide, use modern typing features, and follow standard conventions for command-line tools.

### Scope and Intent

This specification is intended for Python scripts that may be executed directly or integrated into pipelines. It ensures compatibility with modern Python tooling, readability for human developers, and consistency across auto-generated or human-authored code.

### Metadata

```yaml
version: 1.0.0
```

### Imports and Inheritance

* This specification conforms to the Commonmark Markdown specification.
* This specification conforms to the BCP 14 keyword specification.
* The tag symbols Ⓟ, Ⓣ, Ⓔ, and Ⓗ definition and usage conforms to the verification-tags-spec specification.
* The Metadata section conforms to the metadata-spec specification.

### Terminology and Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in all capitals.

### Functional Requirements

* The script MUST be compatible with Python version 3.10 or greater. Ⓟ
* The script MUST declare UTF-8 encoding with a header if non-ASCII characters are used. Ⓟ
* The script MUST use type hints for all function definitions and variables. Ⓟ
* The script MUST conform to PEP 8 style guidelines. Ⓟ
* The script MAY use features from Python 3.10 and later, including structural pattern matching. Ⓗ
* If command-line arguments are required, the script MUST use the `argparse` module. Ⓟ
* If the script defines an entry point, it MUST use a `main()` function guarded by `if __name__ == "__main__":`. Ⓟ
* The script SHOULD include a docstring at the module level describing the purpose and usage. Ⓗ

### Structural Constraints

* The file MUST be a valid UTF-8 encoded `.py` file. Ⓟ
* Top-level code MUST be minimal and limited to guarding the `main()` function. Ⓟ
* Type annotations MUST use standard Python `typing` or built-in syntax (e.g., `list[str]`, `dict[str, int]`). Ⓟ
* The script MUST NOT use wildcard imports. Ⓟ
* Functions and variables SHOULD use lowercase\_with\_underscores naming. Ⓗ
* Classes SHOULD use CapitalizedWords naming. Ⓗ

### Prohibited Elements

* Scripts MUST NOT use deprecated Python 3.10+ features. Ⓟ
* Scripts MUST NOT rely on features that are only available in 3.11+. Ⓟ
* Scripts MUST NOT use non-standard libraries without explicit declaration. Ⓟ
* Scripts MUST NOT contain top-level executable code aside from guarded `main()` calls. Ⓟ
* Scripts MUST NOT include trailing whitespace, tabs for indentation, or inconsistent line endings. Ⓗ

### Verification

**Ⓟ Provable items**:

* UTF-8 encoding declaration
* Use of `argparse` and Python 3.10+ syntax
* Presence and structure of `main()` and `if __name__ == "__main__"` block
* Use of `.py` extension and valid syntax
* PEP 8 style compliance
* Completeness and clarity of type hints

**Ⓗ Heuristically Acceptable items**:

* Docstring presence and clarity

**Ⓣ Testable items**:
N/A

**Ⓔ Evaluatable items**:
N/A

