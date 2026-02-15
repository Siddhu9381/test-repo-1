import pytest
from unittest.mock import Mock, patch
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self) -> dict:
        """
        Convert user to dictionary.
        
        Overrides parent class method to include user-specific fields.
        
        Returns:
            Dictionary representation of the user
        """
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name,
            'email': self.email
        })
        return base_dict

# Saving reference for spec as required
_RealBaseModel = BaseModel
_Realto_dict = BaseModel.to_dict

@patch(f'{__name__}.BaseModel.to_dict')
def test_to_dict_success(mock_super_to_dict):
    # Setup mock for base_dict using the required pattern
    mock_base_dict = Mock()
    mock_base_dict.update.return_value = None
    mock_super_to_dict.return_value = mock_base_dict
    
    # Initialize instance with realistic data
    user = User(name="Jane Doe", email="jane.doe@example.com")
    
    # Execute function under test
    result = user.to_dict()
    
    # Assertions
    assert result == mock_base_dict
    mock_super_to_dict.assert_called_once()
    mock_base_dict.update.assert_called_once_with({
        'name': "Jane Doe",
        'email': "jane.doe@example.com"
    })

@patch(f'{__name__}.BaseModel.to_dict')
def test_to_dict_edge_cases(mock_super_to_dict):
    # Setup mock for base_dict
    mock_base_dict = Mock()
    mock_base_dict.update.return_value = None
    mock_super_to_dict.return_value = mock_base_dict
    
    # Edge case: Empty strings and None values
    user = User(name="", email=None)
    
    # Execute
    result = user.to_dict()
    
    # Assertions
    assert result == mock_base_dict
    mock_base_dict.update.assert_called_once_with({
        'name': "",
        'email': None
    })

@patch(f'{__name__}.BaseModel.to_dict')
def test_to_dict_error(mock_super_to_dict):
    # Error path: super().to_dict() raises an exception
    mock_super_to_dict.side_effect = Exception("Parent method failure")
    
    user = User(name="Test User", email="test@example.com")
    
    # Assert exception propagates
    with pytest.raises(Exception) as exc_info:
        user.to_dict()
    
    assert str(exc_info.value) == "Parent method failure"
    mock_super_to_dict.assert_called_once()