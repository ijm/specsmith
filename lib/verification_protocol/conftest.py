import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "warn: mark test to warn about something"
    )

pytest_plugins= ["pytest_plugin"]

print("loaded cong!")