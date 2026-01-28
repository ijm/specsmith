"""Pytest configuration and fixtures for verification protocol tests."""

#  import pytest

# Ensure the package is in the Python path for testing
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

# Import the pytest plugin
pytest_plugins = ['verification_protocol.pytest_plugin']
