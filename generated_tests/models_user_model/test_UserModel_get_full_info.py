import pytest
from unittest.mock import MagicMock
from datetime import datetime

def get_full_info(self) -> str:
    """
    Get full user information as a formatted string.
    
    Returns:
        Formatted string with user information
    """
    return f"User: {self.name} ({self.email}) - ID: {self.id}"

def test_get_full_info_success():
    """Test the formatted string output with valid, standard data."""
    # Mocking 'self' with realistic test data
    mock_user = MagicMock()
    mock_user.name = "Alice Johnson"
    mock_user.email = "alice.j@example.com"
    mock_user.id = 1001
    
    # Execute the function with the mock instance
    result = get_full_info(mock_user)
    
    # Assert the output matches the expected format
    assert result == "User: Alice Johnson (alice.j@example.com) - ID: 1001"
    assert isinstance(result, str)

def test_get_full_info_edge_cases():
    """Test the function with empty strings, None values, and boundary IDs."""
    mock_user = MagicMock()
    
    # Scenario 1: Empty strings and zero ID
    mock_user.name = ""
    mock_user.email = ""
    mock_user.id = 0
    assert get_full_info(mock_user) == "User:  () - ID: 0"
    
    # Scenario 2: Unicode characters and large integer ID
    mock_user.name = "Müller"
    mock_user.email = "muller@domain.de"
    mock_user.id = 9999999999
    assert get_full_info(mock_user) == "User: Müller (muller@domain.de) - ID: 9999999999"
    
    # Scenario 3: None values (f-strings convert None to 'None')
    mock_user.name = None
    mock_user.email = None
    mock_user.id = None
    assert get_full_info(mock_user) == "User: None (None) - ID: None"

def test_get_full_info_error():
    """Test error handling when attributes are missing or the object is invalid."""
    # Scenario 1: Mocking an object that lacks the required attributes
    # Using spec=[] forces an AttributeError when accessing any attribute not explicitly defined
    mock_user = MagicMock(spec=[])
    
    with pytest.raises(AttributeError):
        get_full_info(mock_user)
        
    # Scenario 2: Passing None as self
    with pytest.raises(AttributeError):
        get_full_info(None)
        
    # Scenario 3: Attribute access raises a generic Exception
    mock_faulty = MagicMock()
    type(mock_faulty).name = property(MagicMock(side_effect=RuntimeError("Database connection failed")))
    
    with pytest.raises(RuntimeError) as excinfo:
        get_full_info(mock_faulty)
    assert "Database connection failed" in str(excinfo.value)