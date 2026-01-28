# Verification Protocol

A Python package for managing and verifying code and specifications and test results using a minimalist structured logging-like protocol.

This module defines a minimal, line-oriented interface for reporting the
status of tests or verification steps.  The format is intentionally simple, human-readable, and easy to parse, following ideas from TAP and syslog rather than all the machinery of JSON.

Each message is a single line with a fixed field order:

    STATUS TEST_NAME SOURCE_REF [MESSAGE]

STATUS is one of PASS, INFO, WARN, FAIL, CRIT, NIMP. TEST_NAME is alphanumeric or a quoted string. SOURCE_REF is of the form source:line. MESSAGE is optional and must not contain newlines.

Messages are represented by an immutable `VerificationMessage` dataclass
with built-in validation, parsing, and serialization. Protocol or validation
errors raise `VerificationError` carrying a structured message.

## Installation

### From Source

1. Clone the repository:

       git clone https://github.com/ijm/verification-protocol.git
       cd verification-protocol
       pip install -e .

### Running Tests

Run the full test suite with coverage:

       ./scripts/run_tests.sh

This will run unit tests with pytest, style checks with flake8, type checking with mypy.

### Pytest Plugin

The package includes a pytest plugin that automatically formats test results as verification protocol messages. To use it, simply install the package and run your tests with pytest:

### unittest Plugin-ish

The package also includes a unittest plugin that automatically formats test results as verification protocol messages.

## License

MIT - See [LICENSE](LICENSE) for more information.
