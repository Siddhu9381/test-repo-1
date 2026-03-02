import pytest
from unittest.mock import Mock, patch
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, name=None, email=None):
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

# Save references before patching as required
_RealBaseModel = BaseModel
_Realto_dict = BaseModel.to_dict

def test_to_dict_success():
    # Setup mocks
    # Saving reference and using Mock() as per instructions
    mock_base_dict = Mock() 
    mock_base_dict.update.return_value = None  # dict.update returns None
    
    # Patch the parent method on the class in the test module's namespace
    with patch(f'{__name__}.BaseModel.to_dict', return_value=mock_base_dict):
        user = User(name="Senior Dev", email="senior@example.com")
        
        # Execute
        result = user.to_dict()
        
        # Assert
        assert result == mock_base_dict
        mock_base_dict.update.assert_called_once_with({
            'name': 'Senior Dev',
            'email': 'senior@example.com'
        })

def test_to_dict_edge_cases():
    # Setup for edge cases: empty strings and None values
    # super().to_dict() returns an empty dictionary
    with patch(f'{__name__}.BaseModel.to_dict', return_value={}):
        user = User(name="", email=None)
        
        # Execute
        result = user.to_dict()
        
        # Assert
        expected = {'name': '', 'email': None}
        assert result == expected
        assert result['name'] == ""
        assert result['email'] is None
        assert isinstance(result, dict)

def test_to_dict_error():
    # Setup for error path: parent method raises an exception
    # Use patch for isolation
    with patch(f'{__name__}.BaseModel.to_dict', side_effect=RuntimeError("BaseModel conversion failed")):
        user = User(name="Error User", email="error@test.com")
        
        # Execute and Assert
        with pytest.raises(RuntimeError) as exc_info:
            user.to_dict()
        
        assert str(exc_info.value) == "BaseModel conversion failed"
        assert exc_info.type is RuntimeError