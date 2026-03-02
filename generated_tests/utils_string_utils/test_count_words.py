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
    # Setup mock for text dependency
    mock_text = Mock()
    mock_text.split.return_value = ["senior", "python", "developer"]
    
    # Execute function under test
    result = count_words(mock_text)
    
    # Assertions
    assert result == 3
    assert isinstance(result, int)
    mock_text.split.assert_called_once()

def test_count_words_edge_cases():
    # Setup mock for empty text scenario
    mock_text = Mock()
    mock_text.split.return_value = []
    
    # Execute function under test
    result = count_words(mock_text)
    
    # Assertions
    assert result == 0
    mock_text.split.assert_called_once()

def test_count_words_error():
    # Setup mock to simulate an error (e.g., if split is called on incompatible object)
    mock_text = Mock()
    mock_text.split.side_effect = AttributeError("Mock object has no attribute split")
    
    # Execute and Assert exception handling
    with pytest.raises(AttributeError) as exc_info:
        count_words(mock_text)
    
    assert "Mock object has no attribute split" in str(exc_info.value)
    mock_text.split.assert_called_once()