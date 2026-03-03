import pytest
from unittest.mock import patch, MagicMock
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

@patch(f'{__name__}.BaseModel.__init__')
def test___init___success(mock_base_init):
    # Happy path with normal inputs
    mock_base_init.return_value = None
    test_name = "John Doe"
    test_email = "john.doe@example.com"
    test_id = "user-123"

    user = UserModel(name=test_name, email=test_email, id=test_id)

    assert user.name == test_name
    assert user.email == test_email
    mock_base_init.assert_called_once_with(test_id)

@patch(f'{__name__}.BaseModel.__init__')
def test___init___edge_cases(mock_base_init):
    # Edge cases: empty strings and None values
    mock_base_init.return_value = None
    
    # Test with empty strings and no ID
    user_empty = UserModel(name="", email="", id=None)
    assert user_empty.name == ""
    assert user_empty.email == ""
    mock_base_init.assert_called_with(None)

    # Test with very long strings
    long_name = "A" * 255
    long_email = "B" * 255 + "@example.com"
    user_long = UserModel(name=long_name, email=long_email, id="id-000")
    assert user_long.name == long_name
    assert user_long.email == long_email
    mock_base_init.assert_called_with("id-000")

@patch(f'{__name__}.BaseModel.__init__')
def test___init___error(mock_base_init):
    # Exception handling: simulate parent class constructor failure
    mock_base_init.side_effect = TypeError("ID must be a string")
    
    with pytest.raises(TypeError) as exc_info:
        UserModel(name="Test User", email="test@example.com", id=12345)
    
    assert str(exc_info.value) == "ID must be a string"
    mock_base_init.assert_called_once_with(12345)