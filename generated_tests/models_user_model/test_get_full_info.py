import pytest
from unittest.mock import Mock, PropertyMock
from datetime import datetime

# Function under test
def get_full_info(self) -> str:
    """
    Get full user information as a formatted string.
    
    Returns:
        Formatted string with user information
    """
    return f"User: {self.name} ({self.email}) - ID: {self.id}"

def test_get_full_info_success():
    """
    Test the happy path with normal string inputs and expected formatting.
    """
    # Setup mock with realistic data
    mock_user = Mock(spec=['name', 'email', 'id'])
    mock_user.name = "John Doe"
    mock_user.email = "john.doe@example.com"
    mock_user.id = "USR-12345"
    
    # Execute the function
    result = get_full_info(mock_user)
    
    # Assertions
    assert result == "User: John Doe (john.doe@example.com) - ID: USR-12345"
    assert isinstance(result, str)
    assert "John Doe" in result
    assert "USR-12345" in result

def test_get_full_info_edge_cases():
    """
    Test edge cases including empty strings, None values, and numeric boundaries.
    """
    mock_user = Mock(spec=['name', 'email', 'id'])
    
    # Case 1: Empty strings
    mock_user.name = ""
    mock_user.email = ""
    mock_user.id = ""
    assert get_full_info(mock_user) == "User:  () - ID: "
    
    # Case 2: None values (Python f-strings convert None to the string 'None')
    mock_user.name = None
    mock_user.email = None
    mock_user.id = None
    assert get_full_info(mock_user) == "User: None (None) - ID: None"
    
    # Case 3: Numeric ID and special characters in name
    mock_user.name = "Admin & User"
    mock_user.email = "admin@system.local"
    mock_user.id = 0
    result = get_full_info(mock_user)
    assert "ID: 0" in result
    assert "Admin & User" in result

def test_get_full_info_error():
    """
    Test exception handling and error paths when attributes are missing or raise exceptions.
    """
    # Scenario 1: Mocking an object that lacks the required attributes (AttributeError)
    mock_invalid_user = Mock(spec=[])
    with pytest.raises(AttributeError):
        get_full_info(mock_invalid_user)
        
    # Scenario 2: Mocking an attribute that raises an exception during access
    mock_faulty_user = Mock(spec=['name', 'email', 'id'])
    # We use PropertyMock to simulate an exception when the 'email' property is accessed
    type(mock_faulty_user).email = PropertyMock(side_effect=RuntimeError("Database connection failed"))
    
    with pytest.raises(RuntimeError, match="Database connection failed"):
        get_full_info(mock_faulty_user)

    # Scenario 3: Verify behavior when name is not a string (f-string should handle it)
    mock_user_types = Mock(spec=['name', 'email', 'id'])
    mock_user_types.name = 12345
    mock_user_types.email = ["test@test.com"]
    mock_user_types.id = {"key": "val"}
    result = get_full_info(mock_user_types)
    assert "12345" in result
    assert "['test@test.com']" in result