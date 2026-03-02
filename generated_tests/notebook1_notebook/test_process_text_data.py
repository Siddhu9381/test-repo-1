import pytest
from unittest.mock import patch

def capitalize_words(text):
    """Placeholder for utility function."""
    pass

def reverse_string(text):
    """Placeholder for utility function."""
    pass

def count_words(text):
    """Placeholder for utility function."""
    pass

def process_text_data(text):
    """
    Process text data using imported string utilities.
    """
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
    # Setup mock return values
    mock_capitalize.return_value = "Python Testing"
    mock_reverse.return_value = "gnitset nohtyp"
    mock_count.return_value = 2
    
    input_text = "python testing"
    
    # Execute
    result = process_text_data(input_text)
    
    # Assertions
    assert result['original'] == input_text
    assert result['capitalized'] == "Python Testing"
    assert result['reversed'] == "gnitset nohtyp"
    assert result['word_count'] == 2
    
    mock_capitalize.assert_called_once_with(input_text)
    mock_reverse.assert_called_once_with(input_text)
    mock_count.assert_called_once_with(input_text)

@patch(f'{__name__}.count_words')
@patch(f'{__name__}.reverse_string')
@patch(f'{__name__}.capitalize_words')
def test_process_text_data_edge_cases(mock_capitalize, mock_reverse, mock_count):
    # Setup for empty string scenario
    mock_capitalize.return_value = ""
    mock_reverse.return_value = ""
    mock_count.return_value = 0
    
    input_text = ""
    
    # Execute
    result = process_text_data(input_text)
    
    # Assertions
    assert result['original'] == ""
    assert result['capitalized'] == ""
    assert result['reversed'] == ""
    assert result['word_count'] == 0
    
    # Setup for single character scenario
    mock_capitalize.return_value = "A"
    mock_reverse.return_value = "a"
    mock_count.return_value = 1
    
    result_single = process_text_data("a")
    assert result_single['word_count'] == 1
    assert result_single['capitalized'] == "A"

@patch(f'{__name__}.capitalize_words')
def test_process_text_data_error(mock_capitalize):
    # Setup mock to raise an exception for invalid input types
    mock_capitalize.side_effect = TypeError("Input must be a string")
    
    # Execute and Assert
    with pytest.raises(TypeError) as exc_info:
        process_text_data(None)
    
    assert str(exc_info.value) == "Input must be a string"
    mock_capitalize.assert_called_once_with(None)