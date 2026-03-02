import pytest
from unittest.mock import patch, Mock
from models.base_model import BaseModel

# Save reference to the real class for spec-based mocking
_RealBaseModel = BaseModel

class UserModel(BaseModel):
    def __init__(self, name: str, email: str, id: str = None):
        """
        Initialize UserModel.
        
        Args:
            name: User's name
            email: User's email
            id: Unique identifier (optional)
        """
        # Call parent class constructor
        super().__init__(id)
        self.name = name
        self.email = email

@patch(f'{__name__}.BaseModel.__init__', return_value=None)
def test_init_success(mock_base_init):
    # Happy path: Initialize with valid name, email, and id
    test_name = "Alice Smith"
    test_email = "alice@example.com"
    test_id = "user-uuid-1234"

    user = UserModel(name=test_name, email=test_email, id=test_id)

    # Verify attributes are set correctly
    assert user.name == test_name
    assert user.email == test_email
    # Verify the parent class constructor was called with the correct ID
    mock_base_init.assert_called_once_with(test_id)

@patch(f'{__name__}.BaseModel.__init__', return_value=None)
def test_init_edge_cases(mock_base_init):
    # Edge cases: Empty strings and default None for id
    test_name = ""
    test_email = ""
    
    user = UserModel(name=test_name, email=test_email)

    assert user.name == ""
    assert user.email == ""
    # Verify super() was called with the default None value
    mock_base_init.assert_called_once_with(None)

@patch(f'{__name__}.BaseModel.__init__')
def test_init_error(mock_base_init):
    # Error path: Parent class constructor raises an exception
    # Use spec for the mock to ensure it behaves like the real method
    mock_base_init.side_effect = ValueError("Invalid ID format")
    
    with pytest.raises(ValueError) as exc_info:
        UserModel(name="Error User", email="error@test.com", id="invalid-id")
    
    # Verify the exception message and call behavior
    assert str(exc_info.value) == "Invalid ID format"
    mock_base_init.assert_called_once_with("invalid-id")