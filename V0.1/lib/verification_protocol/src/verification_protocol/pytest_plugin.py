import sys
from typing import TextIO, Self
from html import escape
from warnings import WarningMessage

import pytest
from _pytest.config import Config, create_terminal_writer
from _pytest.reports import TestReport, CollectReport

from .verification_protocol import VerificationMessage

class VerificationReporter:
    def __init__(self: Self, config: Config, file: TextIO | None) -> None:
        self.config = config
        self._tw = create_terminal_writer(config, file or sys.stdout)

    @pytest.hookimpl(tryfirst=True)
    def pytest_warning_recorded(
        self: Self,
        warning_message: WarningMessage,
        nodeid: str,
    ) -> None:
        (file_name, test_name) = nodeid.split("::")

        self._tw.line(str(
            VerificationMessage(
                status="WARN",
                test_name=test_name,
                source_ref=f"{file_name}:{warning_message.lineno}",
                message=str(warning_message.message),
            )))


    @pytest.hookimpl
    def pytest_report_teststatus(self: Self) -> tuple[str, str, str]:
        # Suppress default dots/F/E
        return "", "", ""

    @pytest.hookimpl
    def pytest_runtest_logreport(self: Self, report: TestReport):
        # Only process the call phase (actual test execution)
        if report.when != "call":
            return
        status = self._map_status(report)
        (file_name, line_number, test_name) = report.location
        source_ref = f"{file_name}:{line_number}"
        message = None

        if report.failed:
            message = getattr(
                getattr(
                    getattr(report, 'longrepr', None),
                    'reprcrash', None),
                'message', "Unknown failure")
        elif report.skipped and report.wasxfail:
            # xfail that passed unexpectedly
            message = "Unexpected success"

        self._tw.line(str(
            VerificationMessage(
                status=status,
                test_name=test_name,
                source_ref=source_ref,
                message=escape(message) if message else None,
            )))

    def _map_status(self: Self, report: TestReport | CollectReport):
        """
        Map a pytest TestReport or CollectReport to verification protocol status.
        """
        # deselected items are only seen in pytest_deselected hook, not here
        # handle runtime/collection/setup errors:

        if report.outcome == "failed" and report.when != "call":
            return "CRIT"  # fixture/setup error should abort testing

        # expected failure (xfail)
        if getattr(report, "wasxfail", False):
            if report.failed:
                return "PASS"  # expected failure occurred
            if report.passed:
                return "FAIL"  # xfail but test passed unexpectedly (xpassed)

        # skipped
        if report.skipped:
            return "NIMP"  # not implemented skip

        # warnings: pytest collects warnings separately but we can detect them
        if getattr(report, "outcome", "") == "warnings":
            return "WARN"

        # error outside call phase (collection/setup/teardown)
        if report.outcome == "error":
            return "CRIT"

        # normal outcomes
        if report.passed:
            return "PASS"

        if report.failed:
            # check for custom markers on node if available
            node = getattr(report, "node", None)
            if node is not None:
                markers = getattr(node, "own_markers", [])
                if any(m.name == "warn" for m in markers):
                    return "WARN"
                if any(m.name == "crit" for m in markers):
                    return "CRIT"
            return "FAIL"

        return "INFO"

    @pytest.hookimpl
    def pytest_terminal_summary(self: Self) -> None:
        pass


def pytest_configure(config: Config) -> None:
    """Configure the verification reporter."""
    # Disable the default warning summary
    config.option.disable_warnings = True
    config.option.tbstyle = "no"

    # Register our custom reporter
    reporter = VerificationReporter(config, sys.stdout)
    config.pluginmanager.register(reporter, "verification-reporter")

    config.addinivalue_line(
        "markers",
        "crit: Critical failures"
    )


def pytest_sessionstart(session: pytest.Session) -> None:
    """Unregister the default terminal reporter at session start."""
    terminalreporter = session.config.pluginmanager.get_plugin('terminalreporter')
    if terminalreporter:
        session.config.pluginmanager.unregister(terminalreporter)
