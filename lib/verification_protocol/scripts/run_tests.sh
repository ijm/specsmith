#!/bin/bash

# Exit on error
set -e

# Go to the project root
cd "$(dirname "${BASH_SOURCE[0]}")/.."

# Run tests
python -m pytest tests/ -v

# Check code style
echo -e "\n\n--- Checking code style ---\n"
python -m flake8 src/verification_protocol tests/

# Run type checking
echo -e "\n\n--- Type checking ---\n"
python -m mypy src/verification_protocol tests/
