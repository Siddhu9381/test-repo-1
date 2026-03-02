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
    # Setup mock instance with standard string data
    mock_instance = Mock()
    mock_instance.data = "valid_test_payload"
    
    # Execute the function
    result = process(mock_instance)
    
    # Assertions
    assert result == "Processed: valid_test_payload"
    assert isinstance(result, str)
    assert "Processed:" in result

def test_process_edge_cases():
    # Case 1: Empty string
    mock_instance_empty = Mock()
    mock_instance_empty.data = ""
    assert process(mock_instance_empty) == "Processed: "
    
    # Case 2: None value (f-string converts None to 'None')
    mock_instance_none = Mock()
    mock_instance_none.data = None
    assert process(mock_instance_none) == "Processed: None"
    
    # Case 3: Numeric boundary (integer)
    mock_instance_int = Mock()
    mock_instance_int.data = 0
    assert process(mock_instance_int) == "Processed: 0"
    
    # Case 4: Special characters
    mock_instance_special = Mock()
    mock_instance_special.data = "!@#$%^&*()"
    assert process(mock_instance_special) == "Processed: !@#$%^&*()"

def test_process_error():
    # Case 1: Attribute does not exist on the object
    # Using spec=[] ensures the Mock doesn't dynamically create the 'data' attribute
    mock_instance_no_attr = Mock(spec=[])
    with pytest.raises(AttributeError):
        process(mock_instance_no_attr)
        
    # Case 2: self is None
    with pytest.raises(AttributeError):
        process(None)
        
    # Case 3: Data attribute exists but string conversion fails
    mock_bad_data = Mock()
    mock_bad_data.__str__.side_effect = ValueError("String conversion error")
    mock_instance_fail = Mock()
    mock_instance_fail.data = mock_bad_data
    with pytest.raises(ValueError):
        process(mock_instance_fail)