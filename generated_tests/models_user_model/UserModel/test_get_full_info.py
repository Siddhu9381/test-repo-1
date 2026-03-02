import pytest
from unittest.mock import MagicMock, PropertyMock
from models.base_model import BaseModel

# Save reference to the real class for spec-based mocking
_RealBaseModel = BaseModel

def test_get_full_info_success():
    """
    Test the happy path with standard user information.
    """
    # Create a mock instance of the class
    mock_user = MagicMock(spec=_RealBaseModel)
    mock_user.name = "John Doe"
    mock_user.email = "john.doe@example.com"
    mock_user.id = "USR-1001"
    
    # Execute the method using the real implementation but a mock 'self'
    result = _RealBaseModel.get_full_info(mock_user)
    
    # Assertions
    assert result == "User: John Doe (john.doe@example.com) - ID: USR-1001"
    assert isinstance(result, str)
    assert "John Doe" in result
    assert "USR-1001" in result

def test_get_full_info_edge_cases():
    """
    Test edge cases including empty strings, numeric boundaries, and None values.
    """
    mock_user = MagicMock(spec=_RealBaseModel)
    
    # Case 1: Empty strings and zero ID
    mock_user.name = ""
    mock_user.email = ""
    mock_user.id = 0
    
    result_empty = _RealBaseModel.get_full_info(mock_user)
    assert result_empty == "User:  () - ID: 0"
    
    # Case 2: None values (f-strings will cast None to 'None')
    mock_user.name = "Admin"
    mock_user.email = None
    mock_user.id = None
    
    result_none = _RealBaseModel.get_full_info(mock_user)
    assert result_none == "User: Admin (None) - ID: None"
    
    # Case 3: Special characters in name/email
    mock_user.name = "O'Connor-Smith"
    mock_user.email = "test+filter@domain.co.uk"
    mock_user.id = 999999999
    
    result_special = _RealBaseModel.get_full_info(mock_user)
    assert result_special == "User: O'Connor-Smith (test+filter@domain.co.uk) - ID: 999999999"

def test_get_full_info_error():
    """
    Test error scenarios where attribute access might fail.
    """
    mock_user = MagicMock(spec=_RealBaseModel)
    
    # Simulate an AttributeError when accessing 'name'
    # This mimics a scenario where the attribute might be missing or deleted
    del mock_user.name
    
    with pytest.raises(AttributeError):
        _RealBaseModel.get_full_info(mock_user)
        
    # Simulate a more complex error using PropertyMock
    # This mimics a property getter raising an exception (e.g., database failure)
    mock_user = MagicMock(spec=_RealBaseModel)
    type(mock_user).email = PropertyMock(side_effect=RuntimeError("Connection lost"))
    
    with pytest.raises(RuntimeError, match="Connection lost"):
        _RealBaseModel.get_full_info(mock_user)