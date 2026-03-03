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
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Senior Developer") == "repoleveD roineS"
    assert reverse_string("1234567890") == "0987654321"
    assert reverse_string("Mixed CASE string") == "gnirts ESAC dexiM"

def test_reverse_string_edge_cases():
    """None, empty values, boundaries, and palindromes."""
    # Empty string
    assert reverse_string("") == ""
    # Single character
    assert reverse_string("A") == "A"
    # String with only whitespace
    assert reverse_string("   ") == "   "
    # Palindrome string
    assert reverse_string("level") == "level"
    # String with special characters and escape sequences
    assert reverse_string("word\nnext") == "txen\ndrow"

def test_reverse_string_error():
    """Exception handling and error paths for invalid types."""
    # Passing None - raises TypeError because None is not subscriptable
    with pytest.raises(TypeError):
        reverse_string(None)
    
    # Passing an integer - raises TypeError because int is not subscriptable
    with pytest.raises(TypeError):
        reverse_string(404)
        
    # Passing a list - while subscriptable, the prompt specifies str input
    # In pure Python, list[::-1] works, but we test typical str-only expectations or type errors
    # if the function logic were to enforce types. Here, we test the inherent behavior.
    # We verify that passing a non-subscriptable object like an object instance fails.
    class Unsubscriptable:
        pass
    
    with pytest.raises(TypeError):
        reverse_string(Unsubscriptable())