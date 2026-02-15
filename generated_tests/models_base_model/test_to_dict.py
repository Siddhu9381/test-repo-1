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
    # Setup: Create a mock object to represent 'self'
    mock_model = Mock()
    mock_model.id = 500
    mock_model.created_at = "2023-12-25 08:00:00"
    
    # Execute: Call the function with the mock instance
    result = to_dict(mock_model)
    
    # Assert: Verify dictionary keys and values
    expected = {
        'id': 500,
        'created_at': "2023-12-25 08:00:00"
    }
    assert result == expected
    assert isinstance(result, dict)
    assert result['id'] == 500
    assert result['created_at'] == "2023-12-25 08:00:00"

def test_to_dict_edge_cases():
    # Setup: Mock instance with empty and None values
    mock_model = Mock()
    
    # Test case: None values
    mock_model.id = None
    mock_model.created_at = None
    result_none = to_dict(mock_model)
    assert result_none['id'] is None
    assert result_none['created_at'] == "None"
    
    # Test case: Empty strings and falsy values
    mock_model.id = ""
    mock_model.created_at = ""
    result_empty = to_dict(mock_model)
    assert result_empty['id'] == ""
    assert result_empty['created_at'] == ""
    
    # Test case: Boundary numeric values
    mock_model.id = 0
    result_zero = to_dict(mock_model)
    assert result_zero['id'] == 0

def test_to_dict_error():
    # Setup: Mock instance that will raise an AttributeError for a missing field
    # Using spec=[] ensures that any attribute access not explicitly defined raises AttributeError
    mock_model_incomplete = Mock(spec=['created_at'])
    mock_model_incomplete.created_at = "2023-01-01"
    
    with pytest.raises(AttributeError):
        to_dict(mock_model_incomplete)
        
    # Setup: Mock instance where str() conversion fails
    mock_model_broken_str = Mock()
    mock_model_broken_str.id = 1
    # Force the __str__ method of the created_at attribute to raise an exception
    mock_model_broken_str.created_at = Mock()
    mock_model_broken_str.created_at.__str__.side_effect = ValueError("String conversion error")
    
    with pytest.raises(ValueError, match="String conversion error"):
        to_dict(mock_model_broken_str)