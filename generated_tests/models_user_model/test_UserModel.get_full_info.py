import pytest
from unittest.mock import Mock
from models.base_model import BaseModel

_RealBaseModel = BaseModel

def test_get_full_info_success():
    """
    Test the happy path with standard string inputs for name, email, and ID.
    """
    mock_user = Mock(spec=_RealBaseModel)
    mock_user.name = "Alice Smith"
    mock_user.email = "alice.smith@example.com"
    mock_user.id = "USR-12345"
    
    # Execute the method by passing the mock as 'self'
    result = _RealBaseModel.get_full_info(mock_user)
    
    assert result == "User: Alice Smith (alice.smith@example.com) - ID: USR-12345"
    assert isinstance(result, str)

def test_get_full_info_edge_cases():
    """
    Test edge cases including empty strings, numeric IDs, and special characters.
    """
    mock_user = Mock(spec=_RealBaseModel)
    # Testing empty strings and numeric ID type which f-strings should handle
    mock_user.name = ""
    mock_user.email = "admin+test@internal.local"
    mock_user.id = 0
    
    result = _RealBaseModel.get_full_info(mock_user)
    
    assert result == "User:  (admin+test@internal.local) - ID: 0"
    assert result.startswith("User: ")
    assert "ID: 0" in result

def test_get_full_info_error():
    """
    Test error paths, such as missing attributes that would cause an AttributeError.
    """
    mock_user = Mock(spec=_RealBaseModel)
    
    # Simulate a missing attribute on the instance to trigger an AttributeError 
    # when the f-string attempts to access self.name
    if hasattr(mock_user, 'name'):
        del mock_user.name
        
    with pytest.raises(AttributeError):
        _RealBaseModel.get_full_info(mock_user)

    # Test scenario where self is None
    with pytest.raises(AttributeError):
        _RealBaseModel.get_full_info(None)