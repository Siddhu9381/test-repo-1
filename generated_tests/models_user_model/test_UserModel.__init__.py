import pytest
from unittest.mock import patch, Mock
from models.base_model import BaseModel

_RealBaseModel = BaseModel

class UserModel(_RealBaseModel):
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

@patch(f"{__name__}.BaseModel.__init__", return_value=None)
def test_init_success(mock_base_init):
    """Test successful initialization with valid strings and an ID."""
    test_name = "John Doe"
    test_email = "john@example.com"
    test_id = "user-12345"
    
    user = UserModel(name=test_name, email=test_email, id=test_id)
    
    assert user.name == test_name
    assert user.email == test_email
    mock_base_init.assert_called_once_with(test_id)

@patch(f"{__name__}.BaseModel.__init__", return_value=None)
def test_init_edge_cases(mock_base_init):
    """Test initialization with empty strings and missing optional ID."""
    # Test with empty strings and default None for id
    user = UserModel(name="", email="")
    
    assert user.name == ""
    assert user.email == ""
    # super().__init__ should be called with None when id is not provided
    mock_base_init.assert_called_once_with(None)

@patch(f"{__name__}.BaseModel.__init__")
def test_init_error(mock_base_init):
    """Test error propagation when the parent constructor raises an exception."""
    # Simulate an error in the BaseModel constructor (e.g., validation failure)
    mock_base_init.side_effect = ValueError("Invalid ID format")
    
    with pytest.raises(ValueError) as exc_info:
        UserModel(name="Test User", email="test@example.com", id="invalid-id-format")
    
    assert str(exc_info.value) == "Invalid ID format"
    mock_base_init.assert_called_once_with("invalid-id-format")