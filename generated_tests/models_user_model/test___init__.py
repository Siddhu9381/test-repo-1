import pytest
from unittest.mock import patch, Mock
from models.base_model import BaseModel

# Saving reference for spec as per requirements
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
def test_user_model_init_success(mock_base_init):
    # Setup
    test_name = "Jane Doe"
    test_email = "jane.doe@example.com"
    test_id = "uuid-1234"

    # Execute
    user = UserModel(name=test_name, email=test_email, id=test_id)

    # Assert
    assert user.name == test_name
    assert user.email == test_email
    mock_base_init.assert_called_once_with(test_id)

@patch(f'{__name__}.BaseModel.__init__', return_value=None)
def test_user_model_init_edge_cases(mock_base_init):
    # Setup - testing empty strings and None ID
    test_name = ""
    test_email = ""
    test_id = None

    # Execute
    user = UserModel(name=test_name, email=test_email, id=test_id)

    # Assert
    assert user.name == ""
    assert user.email == ""
    mock_base_init.assert_called_once_with(None)

@patch(f'{__name__}.BaseModel.__init__')
def test_user_model_init_error(mock_base_init):
    # Setup - simulate parent class initialization failure
    mock_base_init.side_effect = Exception("Database connection failed during ID validation")

    # Execute & Assert
    with pytest.raises(Exception) as excinfo:
        UserModel(name="Error User", email="error@example.com", id="err-999")
    
    assert str(excinfo.value) == "Database connection failed during ID validation"
    mock_base_init.assert_called_once_with("err-999")