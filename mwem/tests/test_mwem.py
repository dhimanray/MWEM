"""
Unit and regression test for the mwem package.
"""

# Import package, test suite, and other packages as needed
import mwem
import pytest
import sys

def test_mwem_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mwem" in sys.modules
