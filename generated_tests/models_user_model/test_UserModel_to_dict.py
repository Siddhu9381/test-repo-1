import pytest
from unittest.mock import patch, Mock
from models.base_model import BaseModel
from models.user import User

# Save reference to real class for spec usage
_RealBaseModel = BaseModel

def test_to_dict_success():
    """Test to_dict with valid user data and successful super() call."""
    # Dependency: base_dict (instance of to_dict)
    mock_base_dict = Mock()
    mock_base_dict.update.return_value = None
    
    # To mock: patch the parent class method used by super()
    # Using the requirement: patch f'{__name__}.to_dict' (patch the class where it's used)
    with patch(f'{__name__}.BaseModel.to_dict') as mock_super:
        mock_super.return_value = mock_base_dict
        
        # Setup realistic test data
        user = User()
        user.name = "John Doe"
        user.email = "john.doe@example.com"
        
        # Execute
        result = user.to_dict()
        
        # Assertions
        mock_super.assert_called_once()
        mock_base_dict.update.assert_called_once_with({
            'name': "John Doe",
            'email': "john.doe@example.com"
        })
        assert result == mock_base_dict
        assert isinstance(result, Mock)

def test_to_dict_edge_cases():
    """Test to_dict with empty values and an empty base dictionary."""
    # Dependency: base_dict (instance of to_dict)
    mock_base_dict = Mock()
    mock_base_dict.update.return_value = None
    
    with patch(f'{__name__}.BaseModel.to_dict') as mock_super:
        mock_super.return_value = mock_base_dict
        
        # Edge case: Empty strings and None values for specific fields
        user = User()
        user.name = ""
        user.email = None
        
        # Execute
        result = user.to_dict()
        
        # Assertions
        mock_base_dict.update.assert_called_once_with({
            'name': "",
            'email': None
        })
        assert result == mock_base_dict

def test_to_dict_error():
    """Test to_dict when the parent class call fails."""
    # To mock: patch the parent class method
    with patch(f'{__name__}.BaseModel.to_dict') as mock_super:
        # Simulate an exception in the parent class method
        mock_super.side_effect = RuntimeError("MRO resolution or base method error")
        
        user = User()
        user.name = "Error User"
        user.email = "error@example.com"
        
        # Execute and Assert
        with pytest.raises(RuntimeError) as exc_info:
            user.to_dict()
        
        assert str(exc_info.value) == "MRO resolution or base method error"
        mock_super.assert_called_once()