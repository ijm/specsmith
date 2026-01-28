import unittest
import sys
import inspect
from verification_protocol import VerificationMessage


def get_source_reference(test: unittest.TestCase) -> str:
    """Return source-id:line-number for the test method."""
    method = getattr(test, test._testMethodName)
    try:
        source_file = inspect.getsourcefile(method) or "<unknown>"
        _, start_line = inspect.getsourcelines(method)
        source_id = source_file.split("/")[-1]  # just filename
        return f"{source_id}:{start_line}"
    except (OSError, TypeError):
        return f"{test.__class__.__name__}:0"


class ProtocolResult(unittest.TextTestResult):
    """Custom TestResult that emits verification protocol lines."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dots = False
        self.showAll = False
        
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write(str(VerificationMessage(
                status="PASS",
                test_name=test._testMethodName,
                source_ref=get_source_reference(test),
            )) + "\n")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.write(str(VerificationMessage(
            status="FAIL",
            test_name=test._testMethodName,
            source_ref=get_source_reference(test),
            message=str(err[1]),
        )) + "\n")

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.write(str(VerificationMessage(
            status="CRIT",
            test_name=test._testMethodName,
            source_ref=get_source_reference(test),
            message=str(err[1]),
        )) + "\n")

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.stream.write(str(VerificationMessage(
            status="INFO",
            test_name=test._testMethodName,
            source_ref=get_source_reference(test),
            message=reason,
        )) + "\n")

    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err)
        self.stream.write(str(VerificationMessage(
            status="PASS",  # treat expected failure as satisfied condition
            test_name=test._testMethodName,
            source_ref=get_source_reference(test),
            message="Expected failure",
        )) + "\n")

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        self.stream.write(str(VerificationMessage(
            status="FAIL",  # treat unexpected success as failure
            test_name=test._testMethodName,
            source_ref=get_source_reference(test),
            message="Unexpected success",
        )) + "\n")
        
    # Override methods that print output
    def printErrors(self):
        pass
        
    def printErrorList(self, *args, **kwargs):
        pass


class ProtocolRunner(unittest.TextTestRunner):
    """Runner that uses ProtocolResult for test execution."""
    def __init__(self, stream=sys.stdout, descriptions=True, verbosity=1, **kwargs):
        super().__init__(stream=stream,
                        descriptions=descriptions,
                        verbosity=verbosity,
                        resultclass=ProtocolResult,
                        **kwargs)


if __name__ == "__main__":
    # Example usage
    class DemoTest(unittest.TestCase):
        def test_pass(self):
            self.assertEqual(1, 1)

        def test_fail(self):
            self.assertEqual(1, 2)

        def test_error(self):
            raise RuntimeError("boom")

        @unittest.skip("not implemented")
        def test_skip(self):
            pass

        @unittest.expectedFailure
        def test_expected_fail(self):
            self.assertEqual(1, 2)

        @unittest.expectedFailure
        def test_unexpected_success(self):
            self.assertEqual(1, 1)

    unittest.main(testRunner=ProtocolRunner, exit=False)
