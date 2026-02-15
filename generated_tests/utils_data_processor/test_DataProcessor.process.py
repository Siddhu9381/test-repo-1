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
    # Happy path: data is a standard string
    mock_self = Mock()
    mock_self.data = "valid_test_data"
    
    result = process(mock_self)
    
    assert result == "Processed: valid_test_data"
    assert isinstance(result, str)

def test_process_edge_cases():
    # Case 1: Empty string as data
    mock_self_empty = Mock()
    mock_self_empty.data = ""
    assert process(mock_self_empty) == "Processed: "
    
    # Case 2: None as data (f-string handles this by calling str(None))
    mock_self_none = Mock()
    mock_self_none.data = None
    assert process(mock_self_none) == "Processed: None"
    
    # Case 3: Numeric data (ensuring implicit string conversion)
    mock_self_numeric = Mock()
    mock_self_numeric.data = 999
    assert process(mock_self_numeric) == "Processed: 999"

def test_process_error():
    # Case 1: The 'self' object is missing the 'data' attribute
    # Using spec=object prevents the Mock from creating attributes on the fly
    mock_invalid_self = Mock(spec=object)
    with pytest.raises(AttributeError):
        process(mock_invalid_self)
        
    # Case 2: The 'self' object is None
    with pytest.raises(AttributeError):
        process(None)
        
    # Case 3: data attribute exists but accessing it raises an exception
    mock_error_self = Mock()
    type(mock_error_self).data = property(Mock(side_effect=RuntimeError("Property access error")))
    with pytest.raises(RuntimeError, match="Property access error"):
        process(mock_error_self)