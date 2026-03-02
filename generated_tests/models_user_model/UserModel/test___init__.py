import pytest
from unittest.mock import patch, Mock
from models.base_model import BaseModel

# Save reference for spec-based mocking
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
    # Happy path with normal inputs
    test_name = "Jane Doe"
    test_email = "jane.doe@example.com"
    test_id = "user-uuid-1234"
    
    user = UserModel(name=test_name, email=test_email, id=test_id)
    
    assert user.name == test_name
    assert user.email == test_email
    # Verify that the parent class constructor was called with the correct ID
    mock_base_init.assert_called_once_with(test_id)

@patch(f'{__name__}.BaseModel.__init__', return_value=None)
def test_init_edge_cases(mock_base_init):
    # None, empty values, boundaries
    # Testing with empty strings and default ID (None)
    test_name = ""
    test_email = ""
    
    user = UserModel(name=test_name, email=test_email)
    
    assert user.name == ""
    assert user.email == ""
    # Verify super class called with None when id is omitted
    mock_base_init.assert_called_once_with(None)

@patch(f'{__name__}.BaseModel.__init__', side_effect=TypeError("ID must be a string"))
def test_init_error(mock_base_init):
    # Exception handling and error paths
    # Simulate a scenario where the base class constructor raises an error
    test_name = "Error User"
    test_email = "error@example.com"
    invalid_id = 12345
    
    with pytest.raises(TypeError) as exc_info:
        UserModel(name=test_name, email=test_email, id=invalid_id)
    
    assert "ID must be a string" in str(exc_info.value)
    mock_base_init.assert_called_once_with(invalid_id)