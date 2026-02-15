import pytest
from unittest.mock import Mock, patch
from models.user_model import UserModel
from utils.string_utils import capitalize_words

_RealUserModel = UserModel

def create_and_format_user(name, email, user_id=None):
    """
    Create a user and format their information.
    
    This function demonstrates using imported classes within a notebook function.
    
    Args:
        name: User's name
        email: User's email
        user_id: Optional user ID
    
    Returns:
        Formatted user information string
    """
    # Use imported UserModel class
    user = UserModel(name, email, user_id)
    
    # Use imported string utility function
    formatted_name = capitalize_words(name)
    
    # Get user info
    user_info = user.get_full_info()
    
    return f"Formatted: {formatted_name} | {user_info}"

@patch(f'{__name__}.capitalize_words')
@patch(f'{__name__}.UserModel')
def test_create_and_format_user_success(mock_user_class, mock_capitalize):
    # Setup mocks
    mock_instance = Mock(spec=_RealUserModel)
    mock_user_class.return_value = mock_instance
    
    mock_capitalize.return_value = "John Doe"
    mock_instance.get_full_info.return_value = "ID: 123 | Name: John Doe | Email: john@example.com"
    
    # Execute
    result = create_and_format_user("john doe", "john@example.com", "123")
    
    # Assert
    assert result == "Formatted: John Doe | ID: 123 | Name: John Doe | Email: john@example.com"
    mock_user_class.assert_called_once_with("john doe", "john@example.com", "123")
    mock_capitalize.assert_called_once_with("john doe")
    mock_instance.get_full_info.assert_called_once()

@patch(f'{__name__}.capitalize_words')
@patch(f'{__name__}.UserModel')
def test_create_and_format_user_edge_cases(mock_user_class, mock_capitalize):
    # Setup mocks for empty/None inputs
    mock_instance = Mock(spec=_RealUserModel)
    mock_user_class.return_value = mock_instance
    
    mock_capitalize.return_value = ""
    mock_instance.get_full_info.return_value = "ID: None | Name:  | Email: "
    
    # Execute with minimal inputs
    result = create_and_format_user("", "", None)
    
    # Assert
    assert result == "Formatted:  | ID: None | Name:  | Email: "
    mock_user_class.assert_called_once_with("", "", None)
    mock_capitalize.assert_called_once_with("")
    mock_instance.get_full_info.assert_called_once()

@patch(f'{__name__}.capitalize_words')
@patch(f'{__name__}.UserModel')
def test_create_and_format_user_error(mock_user_class, mock_capitalize):
    # Setup mocks to simulate an internal failure
    mock_instance = Mock(spec=_RealUserModel)
    mock_user_class.return_value = mock_instance
    
    mock_capitalize.return_value = "Error User"
    # Simulate a runtime error when retrieving full info
    mock_instance.get_full_info.side_effect = RuntimeError("Data retrieval failed")
    
    # Execute and Assert exception handling
    with pytest.raises(RuntimeError) as exc_info:
        create_and_format_user("error user", "error@example.com", "999")
    
    assert str(exc_info.value) == "Data retrieval failed"
    mock_user_class.assert_called_once_with("error user", "error@example.com", "999")
    mock_capitalize.assert_called_once_with("error user")