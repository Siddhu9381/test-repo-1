import pytest
from unittest.mock import patch, Mock

def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: Input string
    
    Returns:
        Reversed string
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]

def test_reverse_string_success():
    """Happy path with normal inputs."""
    # Test standard word
    assert reverse_string("hello") == "olleh"
    
    # Test sentence with spaces
    assert reverse_string("Python is great") == "taerg si nohtyP"
    
    # Test palindrome
    assert reverse_string("racecar") == "racecar"
    
    # Test numeric string
    assert reverse_string("12345") == "54321"

def test_reverse_string_edge_cases():
    """None, empty values, boundaries."""
    # Test empty string
    assert reverse_string("") == ""
    
    # Test single character
    assert reverse_string("a") == "a"
    
    # Test whitespace only
    assert reverse_string("   ") == "   "
    
    # Test special characters and unicode
    assert reverse_string("!@#$%^&*()") == ")(*&^%$#@!"
    assert reverse_string("🚀🔥") == "🔥🚀"

def test_reverse_string_error():
    """Exception handling and error paths."""
    # Test passing None - should raise TypeError because None is not subscriptable
    with pytest.raises(TypeError):
        reverse_string(None)
    
    # Test passing an integer - should raise TypeError
    with pytest.raises(TypeError):
        reverse_string(123)
    
    # Test passing a list
    # While list[::-1] works in Python, the type hint specifies str. 
    # In a strict environment, we ensure it behaves as expected for non-strings.
    input_list = [1, 2, 3]
    assert reverse_string(input_list) == [3, 2, 1] # Slicing works on sequences