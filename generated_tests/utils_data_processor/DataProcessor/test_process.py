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
    """Happy path with normal inputs"""
    # Create a mock object to represent 'self'
    mock_instance = Mock()
    mock_instance.data = "Normal Test Data"
    
    # Execute the function
    result = process(mock_instance)
    
    # Assertions
    assert result == "Processed: Normal Test Data"
    assert isinstance(result, str)
    assert "Processed:" in result

def test_process_edge_cases():
    """None, empty values, boundaries"""
    # Test with an empty string
    mock_empty = Mock()
    mock_empty.data = ""
    assert process(mock_empty) == "Processed: "
    
    # Test with None value
    mock_none = Mock()
    mock_none.data = None
    assert process(mock_none) == "Processed: None"
    
    # Test with numeric data (ensuring f-string handles non-strings)
    mock_numeric = Mock()
    mock_numeric.data = 999.99
    assert process(mock_numeric) == "Processed: 999.99"
    
    # Test with a list
    mock_list = Mock()
    mock_list.data = [1, 2, 3]
    assert process(mock_list) == "Processed: [1, 2, 3]"

def test_process_error():
    """Exception handling and error paths"""
    # Test scenario where 'self' does not have a 'data' attribute
    # Using spec=object ensures the Mock doesn't dynamically create the 'data' attribute
    mock_invalid = Mock(spec=object)
    
    with pytest.raises(AttributeError):
        process(mock_invalid)
        
    # Test scenario where self is None
    with pytest.raises(AttributeError):
        process(None)