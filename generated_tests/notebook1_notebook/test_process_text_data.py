import pytest
from unittest.mock import patch

def capitalize_words(text):
    """Stub for mocking"""
    pass

def reverse_string(text):
    """Stub for mocking"""
    pass

def count_words(text):
    """Stub for mocking"""
    pass

def process_text_data(text):
    """
    Process text data using imported string utilities.
    
    This function demonstrates using imported functions within a notebook function.
    
    Args:
        text: Input text string
    
    Returns:
        Dictionary with processed text information
    """
    # Use imported string utility functions
    capitalized = capitalize_words(text)
    reversed_text = reverse_string(text)
    word_count = count_words(text)
    
    return {
        'original': text,
        'capitalized': capitalized,
        'reversed': reversed_text,
        'word_count': word_count
    }

@patch(f'{__name__}.count_words')
@patch(f'{__name__}.reverse_string')
@patch(f'{__name__}.capitalize_words')
def test_process_text_data_success(mock_capitalize, mock_reverse, mock_count):
    """Test the happy path with standard string input."""
    # Setup mocks
    test_input = "hello world"
    mock_capitalize.return_value = "Hello World"
    mock_reverse.return_value = "dlrow olleh"
    mock_count.return_value = 2
    
    # Execute
    result = process_text_data(test_input)
    
    # Assert
    assert result['original'] == test_input
    assert result['capitalized'] == "Hello World"
    assert result['reversed'] == "dlrow olleh"
    assert result['word_count'] == 2
    
    mock_capitalize.assert_called_once_with(test_input)
    mock_reverse.assert_called_once_with(test_input)
    mock_count.assert_called_once_with(test_input)

@patch(f'{__name__}.count_words')
@patch(f'{__name__}.reverse_string')
@patch(f'{__name__}.capitalize_words')
def test_process_text_data_edge_cases(mock_capitalize, mock_reverse, mock_count):
    """Test edge cases like empty strings and single characters."""
    # Setup mocks for empty string
    test_input = ""
    mock_capitalize.return_value = ""
    mock_reverse.return_value = ""
    mock_count.return_value = 0
    
    # Execute
    result = process_text_data(test_input)
    
    # Assert
    assert result['original'] == ""
    assert result['word_count'] == 0
    assert result['capitalized'] == ""
    
    # Setup mocks for single character
    test_input_single = "a"
    mock_capitalize.return_value = "A"
    mock_reverse.return_value = "a"
    mock_count.return_value = 1
    
    result_single = process_text_data(test_input_single)
    assert result_single['capitalized'] == "A"
    assert result_single['word_count'] == 1

@patch(f'{__name__}.capitalize_words')
def test_process_text_data_error(mock_capitalize):
    """Test error handling when a dependency raises an exception."""
    # Setup mock to raise an error
    test_input = None
    mock_capitalize.side_effect = TypeError("Expected string, got NoneType")
    
    # Execute and Assert
    with pytest.raises(TypeError) as excinfo:
        process_text_data(test_input)
    
    assert "Expected string" in str(excinfo.value)
    mock_capitalize.assert_called_once_with(None)