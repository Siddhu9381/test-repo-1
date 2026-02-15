import pytest
from unittest.mock import Mock, patch
from models.base_model import BaseModel

# Save reference before patching as per requirements
_RealBaseModel = BaseModel
_Real_to_dict = BaseModel.to_dict

class User(BaseModel):
    """
    User class to house the method under test.
    Inherits from BaseModel as specified in the dependencies.
    """
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

@patch(f'{__name__}.BaseModel.to_dict')
def test_to_dict_success(mock_parent_to_dict):
    # Dependency: base_dict (instance of to_dict)
    # To mock: patch the class where it's used
    mock_base_dict = Mock(spec=dict)
    mock_base_dict.update.return_value = None
    mock_parent_to_dict.return_value = mock_base_dict
    
    # Initialize user with normal data
    user = User(name="Senior Developer", email="senior@example.com")
    
    # Execute function under test
    result = user.to_dict()
    
    # Assertions
    assert result == mock_base_dict
    mock_parent_to_dict.assert_called_once()
    mock_base_dict.update.assert_called_once_with({
        'name': "Senior Developer",
        'email': "senior@example.com"
    })

@patch(f'{__name__}.BaseModel.to_dict')
def test_to_dict_edge_cases(mock_parent_to_dict):
    # Setup: Empty base dictionary and None/Empty user attributes
    mock_parent_to_dict.return_value = {}
    user = User(name="", email=None)
    
    # Execute
    result = user.to_dict()
    
    # Assertions for boundary values
    expected = {
        'name': "",
        'email': None
    }
    assert result == expected
    mock_parent_to_dict.assert_called_once()

@patch(f'{__name__}.BaseModel.to_dict')
def test_to_dict_error(mock_parent_to_dict):
    # Setup: Mock dependency to raise an exception
    mock_parent_to_dict.side_effect = RuntimeError("Parent class method failed")
    user = User(name="Error Case", email="error@test.com")
    
    # Execute and Assert exception handling
    with pytest.raises(RuntimeError) as exc_info:
        user.to_dict()
    
    assert str(exc_info.value) == "Parent class method failed"
    mock_parent_to_dict.assert_called_once()