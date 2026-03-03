import pytest
from unittest.mock import Mock

def process(self):
    """
    Process the data.
    
    Returns:
        Processed data
    """
    return f"Processed: {self.data}"

def test_process_success():
    # Happy path: provide a standard string to self.data
    mock_self = Mock()
    mock_self.data = "valid_payload"
    
    result = process(mock_self)
    
    assert result == "Processed: valid_payload"
    assert isinstance(result, str)
    assert "valid_payload" in result

def test_process_edge_cases():
    # Test with empty string
    mock_self_empty = Mock()
    mock_self_empty.data = ""
    assert process(mock_self_empty) == "Processed: "
    
    # Test with None value (f-string converts None to 'None')
    mock_self_none = Mock()
    mock_self_none.data = None
    assert process(mock_self_none) == "Processed: None"
    
    # Test with numeric data
    mock_self_numeric = Mock()
    mock_self_numeric.data = 42
    assert process(mock_self_numeric) == "Processed: 42"

def test_process_error():
    # Test AttributeError: Mock an object that does not have the 'data' attribute
    # Using spec=[] ensures any attribute access not explicitly defined raises AttributeError
    mock_self_invalid = Mock(spec=[])
    with pytest.raises(AttributeError):
        process(mock_self_invalid)
        
    # Test scenario where self is None
    with pytest.raises(AttributeError):
        process(None)