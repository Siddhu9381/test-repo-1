import pytest
from unittest.mock import patch

def capitalize_words(text):
    """Signature for mocking"""
    pass

def reverse_string(text):
    """Signature for mocking"""
    pass

def count_words(text):
    """Signature for mocking"""
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
    # Setup mock return values for the happy path
    mock_capitalize.return_value = "Testing Is Fun"
    mock_reverse.return_value = "nuf si gnitset"
    mock_count.return_value = 3
    
    input_text = "testing is fun"
    
    # Execute function
    result = process_text_data(input_text)
    
    # Assertions
    assert result['original'] == input_text
    assert result['capitalized'] == "Testing Is Fun"
    assert result['reversed'] == "nuf si gnitset"
    assert result['word_count'] == 3
    
    # Verify mocks were called correctly
    mock_capitalize.assert_called_once_with(input_text)
    mock_reverse.assert_called_once_with(input_text)
    mock_count.assert_called_once_with(input_text)

@patch(f'{__name__}.count_words')
@patch(f'{__name__}.reverse_string')
@patch(f'{__name__}.capitalize_words')
def test_process_text_data_edge_cases(mock_capitalize, mock_reverse, mock_count):
    # Setup mock return values for empty string edge case
    mock_capitalize.return_value = ""
    mock_reverse.return_value = ""
    mock_count.return_value = 0
    
    input_text = ""
    
    # Execute function
    result = process_text_data(input_text)
    
    # Assertions
    assert result['original'] == ""
    assert result['capitalized'] == ""
    assert result['reversed'] == ""
    assert result['word_count'] == 0
    
    # Verify calls
    mock_capitalize.assert_called_once_with("")
    mock_count.assert_called_once_with("")

@patch(f'{__name__}.capitalize_words')
def test_process_text_data_error(mock_capitalize):
    # Setup mock to raise an exception to test error handling/propagation
    mock_capitalize.side_effect = ValueError("External utility failed")
    
    # Execute and Assert
    with pytest.raises(ValueError) as exc_info:
        process_text_data("some text")
    
    assert str(exc_info.value) == "External utility failed"
    mock_capitalize.assert_called_once_with("some text")