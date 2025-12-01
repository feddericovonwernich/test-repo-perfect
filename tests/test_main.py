"""
Test suite for the main module.
"""
import pytest


def test_example_pass():
    """Test that always passes."""
    assert True


def test_addition():
    """Test basic addition."""
    assert 1 + 1 == 2


def test_string_operations():
    """Test string operations."""
    assert "hello".upper() == "HELLO"


class TestSampleClass:
    """Sample test class with multiple tests."""

    def test_method_one(self):
        """First test method."""
        assert [] == []

    def test_method_two(self):
        """Second test method."""
        assert {} == {}
