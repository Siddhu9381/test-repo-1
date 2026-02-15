import pytest
from unittest.mock import Mock

def count_words(text: str) -> int:
    """
    Count the number of words in a string.
    
    Args:
        text: Input string
    
    Returns:
        Number of words
    
    Example:
        >>> count_words("hello world")
        2
    """
    return len(text.split())

def test_count_words_success():
    # Dependency: text
    mock_text = Mock()
    mock_text.split.return_value = ["senior", "python", "developer", "test"]
    
    # Execute
    result = count_words(mock_text)
    
    # Assert
    assert result == 4
    assert isinstance(result, int)
    mock_text.split.assert_called_once()

def test_count_words_edge_cases():
    # Dependency: text
    # Test empty string scenario where split() returns an empty list
    mock_text = Mock()
    mock_text.split.return_value = []
    
    # Execute
    result = count_words(mock_text)
    
    # Assert
    assert result == 0
    mock_text.split.assert_called_once()

def test_count_words_error():
    # Dependency: text
    # Test scenario where the input does not support split (e.g., None or wrong type)
    mock_text = Mock()
    mock_text.split.side_effect = AttributeError("object has no attribute 'split'")
    
    # Assert
    with pytest.raises(AttributeError) as excinfo:
        count_words(mock_text)
    
    assert "object has no attribute 'split'" in str(excinfo.value)
    mock_text.split.assert_called_once()