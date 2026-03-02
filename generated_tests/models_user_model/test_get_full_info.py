import pytest
from unittest.mock import Mock, PropertyMock
from models.base_model import BaseModel

def test_get_full_info_success():
    """
    Test the happy path of get_full_info with standard string inputs.
    Verifies that the formatted string correctly incorporates name, email, and ID.
    """
    # Save reference to real class and create a mock instance
    _RealBaseModel = BaseModel
    mock_user = Mock(spec=_RealBaseModel)
    
    # Setup realistic test data
    mock_user.name = "Alice Smith"
    mock_user.email = "alice.smith@example.com"
    mock_user.id = "USR-1001"
    
    # Execute the method using the mock instance as 'self'
    result = _RealBaseModel.get_full_info(mock_user)
    
    # Assertions
    expected = "User: Alice Smith (alice.smith@example.com) - ID: USR-1001"
    assert result == expected
    assert isinstance(result, str)

def test_get_full_info_edge_cases():
    """
    Test edge cases including empty strings, numeric values, and None.
    Verifies the function's behavior with boundary data types and values.
    """
    _RealBaseModel = BaseModel
    mock_user = Mock(spec=_RealBaseModel)
    
    # Case 1: Empty strings and integer ID
    mock_user.name = ""
    mock_user.email = ""
    mock_user.id = 0
    assert _RealBaseModel.get_full_info(mock_user) == "User:  () - ID: 0"
    
    # Case 2: Very long strings
    mock_user.name = "A" * 100
    mock_user.email = "dev@company.international"
    mock_user.id = 999999999
    result = _RealBaseModel.get_full_info(mock_user)
    assert "A" * 100 in result
    assert "999999999" in result
    
    # Case 3: None values (checking f-string default conversion)
    mock_user.name = None
    mock_user.email = None
    mock_user.id = None
    assert _RealBaseModel.get_full_info(mock_user) == "User: None (None) - ID: None"

def test_get_full_info_error():
    """
    Test error scenarios where attribute access might fail.
    Simulates an AttributeError during string formatting, common in ORM lazy-loading failures.
    """
    _RealBaseModel = BaseModel
    mock_user = Mock(spec=_RealBaseModel)
    
    # Use PropertyMock to simulate a failure when the 'email' attribute is accessed
    # This ensures we cover paths where the object state is invalid or inaccessible
    type(mock_user).email = PropertyMock(side_effect=AttributeError("Email attribute not initialized"))
    mock_user.name = "John Doe"
    mock_user.id = "123"
    
    with pytest.raises(AttributeError) as exc_info:
        _RealBaseModel.get_full_info(mock_user)
    
    assert "Email attribute not initialized" in str(exc_info.value)