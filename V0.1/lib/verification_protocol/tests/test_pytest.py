import pytest
import warnings
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# --- PASS ---
def test_pass():
    assert 1 + 1 == 2

# --- FAIL ---
def test_fail():
    assert 1 + 1 == 3

# --- WARN ---
def test_warn():
    warnings.warn("This is a Warning")

# --- CRIT ---
@pytest.mark.crit
def test_crit():
    raise ValueError("Critical failure")

# --- NIMP ---
@pytest.mark.skip(reason="not implemented")
def test_nimp():
    pass

# --- INFO ---
@pytest.mark.skip(reason="informational skip")
def test_info():
    pass

# --- Expected Failure (xfail) ---
@pytest.mark.xfail(raises=AssertionError)
def test_xfail():
    assert False

# --- Unexpected Success (xpass) ---
@pytest.mark.xfail(raises=AssertionError)
def test_xpass():
    assert True
