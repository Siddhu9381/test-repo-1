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
    """Test the happy path where all attributes are standard and valid."""
    mock_model = Mock()
    mock_model.id = 123
    mock_model.created_at = "2023-10-27 14:30:05"
    
    result = to_dict(mock_model)
    
    assert result == {
        'id': 123,
        'created_at': "2023-10-27 14:30:05"
    }
    assert isinstance(result, dict)
    assert result['id'] == 123
    assert result['created_at'] == "2023-10-27 14:30:05"

def test_to_dict_edge_cases():
    """Test edge cases including None values and empty strings."""
    # Case 1: ID is None and created_at is an empty list (testing str() conversion)
    mock_model_null = Mock()
    mock_model_null.id = None
    mock_model_null.created_at = []
    
    result_null = to_dict(mock_model_null)
    assert result_null['id'] is None
    assert result_null['created_at'] == "[]"
    
    # Case 2: ID is a very large integer and created_at is a mock object
    mock_model_large = Mock()
    mock_model_large.id = 999999999999
    mock_model_large.created_at = Mock()
    mock_model_large.created_at.__str__.return_value = "Mocked Date"
    
    result_large = to_dict(mock_model_large)
    assert result_large['id'] == 999999999999
    assert result_large['created_at'] == "Mocked Date"

def test_to_dict_error():
    """Test error paths such as missing attributes or failed string conversion."""
    # Case 1: Missing attribute 'id' on the instance
    mock_invalid_model = Mock(spec=[]) # No attributes allowed
    
    with pytest.raises(AttributeError):
        to_dict(mock_invalid_model)
        
    # Case 2: Failure during string conversion of created_at
    mock_error_model = Mock()
    mock_error_model.id = 1
    # Mocking __str__ to raise an exception
    mock_error_model.created_at = Mock()
    mock_error_model.created_at.__str__.side_effect = ValueError("Format Error")
    
    with pytest.raises(ValueError, match="Format Error"):
        to_dict(mock_error_model)