import pytest
from unittest.mock import Mock

def transform(self, transformation: str):
    """
    Transform the data.
    
    Args:
        transformation: Type of transformation to apply
    
    Returns:
        Transformed data
    """
    return f"Transformed ({transformation}): {self.data}"

def test_transform_success():
    """Happy path with normal inputs."""
    # Create a mock instance to act as 'self'
    mock_instance = Mock()
    mock_instance.data = "raw_payload_data"
    
    # Define a standard transformation type
    transformation_type = "base64_encode"
    
    # Execute the function
    result = transform(mock_instance, transformation_type)
    
    # Assertions
    assert result == "Transformed (base64_encode): raw_payload_data"
    assert isinstance(result, str)
    assert "raw_payload_data" in result

def test_transform_edge_cases():
    """Edge cases: empty values and special characters."""
    mock_instance = Mock()
    
    # Test case 1: Empty strings for both data and transformation
    mock_instance.data = ""
    assert transform(mock_instance, "") == "Transformed (): "
    
    # Test case 2: Special characters and symbols
    mock_instance.data = "§±!@#$%^&*()_+"
    assert transform(mock_instance, "UTF-8") == "Transformed (UTF-8): §±!@#$%^&*()_+"
    
    # Test case 3: Numeric strings as transformation names
    mock_instance.data = "data"
    assert transform(mock_instance, "12345") == "Transformed (12345): data"

def test_transform_error():
    """Exception handling and error paths."""
    # Test case 1: Missing 'data' attribute on the object
    # Using spec=[] ensures the mock does not have any attributes unless added
    mock_invalid_instance = Mock(spec=[])
    
    with pytest.raises(AttributeError):
        # Accessing self.data will raise AttributeError
        transform(mock_invalid_instance, "normalize")
    
    # Test case 2: self is None (NoneType has no attribute 'data')
    with pytest.raises(AttributeError):
        transform(None, "normalize")
        
    # Test case 3: transformation is None
    # f-strings convert None to 'None', so we check if that behavior is consistent
    mock_instance = Mock()
    mock_instance.data = "valid_data"
    assert transform(mock_instance, None) == "Transformed (None): valid_data"