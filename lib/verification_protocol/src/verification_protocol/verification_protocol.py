from dataclasses import dataclass
from typing import Literal, get_args, cast, final
import re

# Define status type and values in one place
StatusType = Literal["PASS", "INFO", "WARN", "FAIL", "CRIT", "NIMP"]
_VALID_STATUSES: set[StatusType] = set(get_args(StatusType))
_TEST_NAME_RE = re.compile(r'^[A-Za-z0-9_-]+|"[^"]+"$')
_SOURCE_REF_RE = re.compile(r'^[^\s:]+:\d+$')

class VerificationError(Exception):
    """Exception raised for protocol or validation errors."""

    def __init__(self, vmsg: 'VerificationMessage'):
        super().__init__(str(vmsg))
        self.vmsg = vmsg

@final
@dataclass(frozen=True)
class VerificationMessage:
    """Structured representation of a verification protocol message."""
    status: StatusType
    test_name: str 
    """Alphanumeric or quoted string"""
    source_ref: str 
    """String of the form ``source:line``"""
    message: str | None = None
    """Optional string message must not contain newline characters"""

    def __post_init__(self) -> None:
        """Validate fields according to spec."""

        # Notes, validation failures will raise a VerificationError with
        # a VerificationMessage() requiring a recursive call to __post_init__,
        # so all strings are literals.

        if self.status not in _VALID_STATUSES:
            raise VerificationError(VerificationMessage(
                status="CRIT",
                test_name="internal-validation-error",
                source_ref="verification-protocol:0",
                message="Invalid status",
            ))

        if not _TEST_NAME_RE.match(self.test_name):
            raise VerificationError(VerificationMessage(
                status="CRIT",
                test_name="internal-validation-error",
                source_ref="verification-protocol:0",
                message="Invalid test_name",
            ))

        if not _SOURCE_REF_RE.match(self.source_ref):
            raise VerificationError(VerificationMessage(
                status="CRIT",
                test_name="internal-validation-error",
                source_ref="verification-protocol:0",
                message="Invalid source_ref",
            ))


        if self.message is not None and '"' in self.message:
            raise VerificationError(VerificationMessage(
                status="CRIT",
                test_name="internal-validation-error",
                source_ref="verification-protocol:0",
                message="Invalid message"
            ))

    def __str__(self):  
        return self.to_string(self)

    @classmethod
    def to_string(cls, vmsg: "VerificationMessage") -> str:
        """ Convert a VerificationMessage to a protocol line. """

        parts = [vmsg.status, vmsg.test_name, vmsg.source_ref]
        if vmsg.message is not None:
            parts.append(vmsg.message)
        return " ".join(parts)

    @classmethod
    def from_string(cls, line: str) -> "VerificationMessage":
        """
        Parse a protocol line into a VerificationMessage.
        Raises with a VerificationError with a VerificationMessage if parsing fails.
        """

        tokens = line.strip().split(maxsplit=3)

        if len(tokens) < 3:
            raise VerificationError(VerificationMessage(
                status="CRIT",
                test_name="internal-parse-error",
                source_ref="verification-protocol:0",
                message="Too few fields in line",
            ))

        status, test_name, source_ref = tokens[:3]

        return VerificationMessage(  # init will validate
            status=cast(StatusType, status), 
            test_name=test_name,
            source_ref=source_ref,
            message=tokens[3] if len(tokens) == 4 else None,
        )
