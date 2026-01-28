"""Verification Protocol - A protocol for verifying specifications and test results."""

from .verification_protocol import VerificationMessage, VerificationError

__all__ = [
    'VerificationMessage',
    'VerificationError',
]

# Set the package version
__version__ = '0.1.0'
