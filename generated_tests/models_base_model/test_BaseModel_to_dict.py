import pytest
from unittest.mock import Mock

def to_dict(self) -> dict:
    """
    Convert model to dictionary.
    
    Returns:
        Dictionary representation of the model
    """
    return {
        'id': self.id,
        'created_at': str(self.created_at)
    }

def test_to_dict_success():
    """Test the happy path with valid id and created_at values."""
    mock_model = Mock()
    mock_model.id = 12345
    mock_model.created_at = "2023-10-27 14:30:05"
    
    # Execute function
    result = to_dict(mock_model)
    
    # Assertions
    assert isinstance(result, dict), "Result should be a dictionary"
    assert result['id'] == 12345, "The id in the dictionary should match the model id"
    assert result['created_at'] == "2023-10-27 14:30:05", "The created_at should be converted to string"
    assert len(result) == 2, "Dictionary should contain exactly two keys"

def test_to_dict_edge_cases():
    """Test edge cases such as None values and empty strings."""
    mock_model = Mock()
    
    # Case 1: None values
    mock_model.id = None
    mock_model.created_at = None
    
    result_none = to_dict(mock_model)
    assert result_none['id'] is None
    assert result_none['created_at'] == "None", "str(None) should result in the string 'None'"
    
    # Case 2: Empty values
    mock_model.id = ""
    mock_model.created_at = ""
    
    result_empty = to_dict(mock_model)
    assert result_empty['id'] == ""
    assert result_empty['created_at'] == "", "Empty string should remain empty string"
    
    # Case 3: Numeric boundary for id
    mock_model.id = 0
    mock_model.created_at = 0
    result_zero = to_dict(mock_model)
    assert result_zero['id'] == 0
    assert result_zero['created_at'] == "0"

def test_to_dict_error():
    """Test exception handling for missing attributes or string conversion failures."""
    mock_model = Mock(spec=[]) # Create mock with no attributes to force AttributeError
    
    # Test AttributeError for missing 'id'
    with pytest.raises(AttributeError):
        to_dict(mock_model)
        
    # Test TypeError or other exceptions during string conversion
    mock_model_error = Mock()
    mock_model_error.id = 1
    # Mock created_at so that calling str() on it raises an error
    mock_model_error.created_at = Mock()
    mock_model_error.created_at.__str__.side_effect = ValueError("String conversion error")
    
    with pytest.raises(ValueError, match="String conversion error"):
        to_dict(mock_model_error)