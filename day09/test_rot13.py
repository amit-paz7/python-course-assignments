# This file contains tests for the ROT13 utility function. To run it, you would use the command: pytest

from rot13_utils import apply_rot13

def test_lowercase_string():
    """Tests an all-lowercase string."""
    assert apply_rot13("hello") == "uryyb"

def test_uppercase_string():
    """Tests an all-uppercase string."""
    assert apply_rot13("WORLD") == "JBEYQ"

def test_mixed_case_string():
    """Tests a string with mixed casing."""
    assert apply_rot13("Python") == "Clguba"

def test_string_with_punctuation_and_numbers():
    """Tests that non-letters are not changed."""
    assert apply_rot13("Test 1, 2, 3!") == "Grfg 1, 2, 3!"

def test_empty_string():
    """Tests that an empty string remains empty."""
    assert apply_rot13("") == ""

def test_double_application():
    """Tests that applying ROT13 twice returns the original string."""
    original = "This is a secret message."
    assert apply_rot13(apply_rot13(original)) == original
