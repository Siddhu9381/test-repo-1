import pytest
from unittest.mock import Mock

def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text: Input string
    
    Returns:
        String with capitalized words
    
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return ' '.join(word.capitalize() for word in text.split())

def test_capitalize_words_success():
    # Dependency: text
    # Mocking the input string object to control the split behavior
    mock_text = Mock()
    mock_text.split.return_value = ['unit', 'testing', 'is', 'fun']
    
    # Execute function with mock
    result = capitalize_words(mock_text)
    
    # Assertions
    assert result == 'Unit Testing Is Fun'
    mock_text.split.assert_called_once()

def test_capitalize_words_edge_cases():
    # Case 1: Empty string (split returns empty list)
    mock_text_empty = Mock()
    mock_text_empty.split.return_value = []
    assert capitalize_words(mock_text_empty) == ""
    
    # Case 2: Single word
    mock_text_single = Mock()
    mock_text_single.split.return_value = ['python']
    assert capitalize_words(mock_text_single) == "Python"
    
    # Case 3: Already capitalized words
    mock_text_caps = Mock()
    mock_text_caps.split.return_value = ['Hello', 'World']
    assert capitalize_words(mock_text_caps) == "Hello World"
    
    # Case 4: Mixed casing
    mock_text_mixed = Mock()
    mock_text_mixed.split.return_value = ['iPHONE', 'mAcBoOk']
    assert capitalize_words(mock_text_mixed) == "Iphone Macbook"

def test_capitalize_words_error():
    # Scenario 1: Input is None (AttributeError on .split())
    # This tests the failure path when the input doesn't adhere to the expected interface
    with pytest.raises(AttributeError):
        capitalize_words(None)
        
    # Scenario 2: split() returns items that are not strings (AttributeError on .capitalize())
    mock_text_invalid_items = Mock()
    mock_text_invalid_items.split.return_value = [123, None]
    with pytest.raises(AttributeError):
        capitalize_words(mock_text_invalid_items)

    # Scenario 3: Input is an integer (AttributeError on .split())
    with pytest.raises(AttributeError):
        capitalize_words(42)