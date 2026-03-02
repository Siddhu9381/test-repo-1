import pytest
from unittest.mock import MagicMock, patch

class DataProcessor:
    def __init__(self, data):
        """
        Initialize DataProcessor with data.
        
        Args:
            data: Data to be processed
        """
        self.data = data

def test_init_success():
    """Happy path with normal inputs."""
    # Create realistic mock data
    mock_payload = {
        "id": 101,
        "payload": "sensor_data",
        "values": [22.5, 23.1, 21.8]
    }
    
    # Initialize the processor
    processor = DataProcessor(data=mock_payload)
    
    # Assertions
    assert processor.data == mock_payload
    assert isinstance(processor.data, dict)
    assert processor.data["id"] == 101

def test_init_edge_cases():
    """None, empty values, boundaries."""
    # Test with None
    processor_none = DataProcessor(None)
    assert processor_none.data is None
    
    # Test with empty list
    processor_list = DataProcessor([])
    assert processor_list.data == []
    
    # Test with empty string
    processor_str = DataProcessor("")
    assert processor_str.data == ""
    
    # Test with integer zero
    processor_zero = DataProcessor(0)
    assert processor_zero.data == 0

def test_init_error():
    """Exception handling and error paths."""
    # Test TypeError when initialized without the required 'data' argument
    with pytest.raises(TypeError) as excinfo:
        DataProcessor()
    assert "missing 1 required positional argument" in str(excinfo.value)
    
    # Test TypeError when initialized with unexpected keyword arguments
    with pytest.raises(TypeError) as excinfo:
        DataProcessor(data="test", extra_arg="unexpected")
    assert "unexpected keyword argument" in str(excinfo.value)