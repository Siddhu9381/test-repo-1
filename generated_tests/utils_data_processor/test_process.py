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
    # Setup mock object to act as 'self'
    mock_self = Mock()
    mock_self.data = "Normal Test Data"
    
    # Execute the function
    result = process(mock_self)
    
    # Assertions
    assert result == "Processed: Normal Test Data"
    assert isinstance(result, str)

def test_process_edge_cases():
    """None, empty values, and boundaries"""
    mock_self = Mock()
    
    # Case 1: Empty string
    mock_self.data = ""
    assert process(mock_self) == "Processed: "
    
    # Case 2: None value
    mock_self.data = None
    assert process(mock_self) == "Processed: None"
    
    # Case 3: Numeric value
    mock_self.data = 0
    assert process(mock_self) == "Processed: 0"
    
    # Case 4: Large string
    long_data = "A" * 1000
    mock_self.data = long_data
    assert process(mock_self) == f"Processed: {long_data}"

def test_process_error():
    """Exception handling and error paths"""
    # Test scenario: self does not have the attribute 'data'
    # Using spec=[] ensures the Mock doesn't dynamically create the 'data' attribute
    mock_self = Mock(spec=[])
    
    with pytest.raises(AttributeError) as exc_info:
        process(mock_self)
    
    assert "data" in str(exc_info.value)

    # Test scenario: data property exists but raises an exception when accessed
    mock_self_with_error = Mock()
    type(mock_self_with_error).data = property(Mock(side_effect=RuntimeError("Data access failed")))
    
    with pytest.raises(RuntimeError) as exc_info:
        process(mock_self_with_error)
    assert str(exc_info.value) == "Data access failed"