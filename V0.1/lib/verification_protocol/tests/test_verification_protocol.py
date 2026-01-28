"""Tests for the verification protocol implementation."""

import sys
import os
from pathlib import Path
from typing import cast
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from verification_protocol.verification_protocol import (
    VerificationMessage, 
    VerificationError,
    StatusType
)


def test_verification_message_creation():
    """Test creating a verification message with valid data."""
    message = VerificationMessage(
        status="PASS",
        test_name="test-example",
        source_ref="test_file.py:42",
        message="Test passed successfully"
    )
    assert message.status == "PASS"
    assert message.test_name == "test-example"
    assert message.source_ref == "test_file.py:42"
    assert message.message == "Test passed successfully"


def test_verification_message_validation():
    """Test validation of verification message fields."""
    # Test valid test names (should not raise)
    valid_names = [
        "test-name",
        "test_name",
        "test123",
        "test.name",
        '"test with spaces"',
        '"test.with.dots"',
    ]
    for name in valid_names:
        VerificationMessage(
            status="PASS",
            test_name=name,
            source_ref="test_file.py:42"
        )
    
    # Test invalid source reference (missing line number)
    with pytest.raises(VerificationError) as exc_info:
        VerificationMessage(
            status="PASS",
            test_name="test-example",
            source_ref="test_file"  # Missing line number
        )
    assert "Invalid source_ref" in str(exc_info.value.vmsg)

    # Test message with quotes
    with pytest.raises(VerificationError) as exc_info:
        VerificationMessage(
            status="PASS",
            test_name="test-example",
            source_ref="test_file.py:42",
            message='Message with "quotes"'
        )
    assert "Invalid message" in str(exc_info.value.vmsg)


def test_verification_message_str():
    """Test string representation of verification message."""
    message = VerificationMessage(
        status="PASS",
        test_name="test-example",
        source_ref="test_file.py:42",
        message="Test passed successfully"
    )
    expected = "PASS test-example test_file.py:42 Test passed successfully"
    assert str(message) == expected

    # Test without message
    message = VerificationMessage(
        status="PASS",
        test_name="test-example",
        source_ref="test_file.py:42"
    )
    assert str(message) == "PASS test-example test_file.py:42"


def test_verification_message_from_string():
    """Test parsing a verification message from a string."""
    # Test with message
    msg = VerificationMessage.from_string(
        "PASS test-example test_file.py:42 Test passed successfully"
    )
    assert msg.status == "PASS"
    assert msg.test_name == "test-example"
    assert msg.source_ref == "test_file.py:42"
    assert msg.message == "Test passed successfully"

    # Test without message
    msg = VerificationMessage.from_string("PASS test-example test_file.py:42")
    assert msg.status == "PASS"
    assert msg.test_name == "test-example"
    assert msg.source_ref == "test_file.py:42"
    assert msg.message is None

    # Test with invalid format
    with pytest.raises(VerificationError):
        VerificationMessage.from_string("INVALID")


def test_verification_error():
    """Test VerificationError with a verification message."""
    vmsg = VerificationMessage(
        status="CRIT",
        test_name="test-error",
        source_ref="test.py:123",
        message="Test error message"
    )
    error = VerificationError(vmsg)
    assert str(error) == str(vmsg)
    assert error.vmsg is vmsg
