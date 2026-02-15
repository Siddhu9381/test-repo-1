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
    """Happy path: Test transformation with standard string inputs."""
    # Arrange
    mock_self = Mock()
    mock_self.data = "original_payload"
    transformation_type = "uppercase"
    expected_output = "Transformed (uppercase): original_payload"

    # Act
    result = transform(mock_self, transformation_type)

    # Assert
    assert result == expected_output
    assert isinstance(result, str)
    assert "original_payload" in result

def test_transform_edge_cases():
    """Edge cases: Test with empty strings, None values, and special characters."""
    mock_self = Mock()

    # Case 1: Empty strings for both data and transformation
    mock_self.data = ""
    assert transform(mock_self, "") == "Transformed (): "

    # Case 2: Special characters and escape sequences
    mock_self.data = "data\nwith\nnewlines"
    result_special = transform(mock_self, "!@#$")
    assert result_special == "Transformed (!@#$): data\nwith\nnewlines"

    # Case 3: Numeric data (f-strings handle implicit string conversion)
    mock_self.data = 99.9
    assert transform(mock_self, "float") == "Transformed (float): 99.9"

    # Case 4: None values (f-strings convert None to the string 'None')
    mock_self.data = None
    assert transform(mock_self, "none_type") == "Transformed (none_type): None"

def test_transform_error():
    """Error path: Test behavior when self is missing the required data attribute."""
    # Arrange: Create a mock that strictly defines allowed attributes (excluding 'data')
    mock_self = Mock(spec=["other_attribute"])
    
    # Act & Assert: Accessing self.data should raise AttributeError
    with pytest.raises(AttributeError):
        transform(mock_self, "any_transformation")

    # Arrange: Test with a transformation object that raises an error during string conversion
    class BrokenString:
        def __str__(self):
            raise ValueError("String conversion error")
            
    mock_valid_self = Mock()
    mock_valid_self.data = "valid_data"
    
    # Act & Assert: F-string interpolation calls __str__, which should propagate the ValueError
    with pytest.raises(ValueError, match="String conversion error"):
        transform(mock_valid_self, BrokenString())