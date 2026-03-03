import pytest
from unittest.mock import Mock

class DataProcessor:
    def __init__(self, data):
        """
        Initialize DataProcessor with data.
        
        Args:
            data: Data to be processed
        """
        self.data = data

def test_init_success():
    """Test successful initialization with standard data objects."""
    # Test with a Mock object to ensure isolation
    mock_data = Mock()
    processor = DataProcessor(data=mock_data)
    assert processor.data == mock_data
    assert processor.data is mock_data

    # Test with standard dictionary
    sample_dict = {"id": 1, "payload": "test_info"}
    processor_dict = DataProcessor(data=sample_dict)
    assert processor_dict.data == sample_dict
    assert processor_dict.data["id"] == 1

def test_init_edge_cases():
    """Test initialization with None, empty values, and boundary inputs."""
    # Test with None
    processor_none = DataProcessor(data=None)
    assert processor_none.data is None

    # Test with empty string
    processor_empty_str = DataProcessor(data="")
    assert processor_empty_str.data == ""

    # Test with empty list
    processor_empty_list = DataProcessor(data=[])
    assert processor_empty_list.data == []
    assert len(processor_empty_list.data) == 0

def test_init_error():
    """Test error conditions for initialization."""
    # Test missing required 'data' argument (TypeError)
    with pytest.raises(TypeError) as excinfo:
        DataProcessor()
    assert "missing 1 required positional argument" in str(excinfo.value)

    # Test unexpected number of arguments
    with pytest.raises(TypeError) as excinfo:
        DataProcessor("data_arg_1", "extra_arg_2")
    assert "takes 2 positional arguments but 3 were given" in str(excinfo.value)