import pytest
from unittest.mock import patch, Mock
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
    mock_user_instance = Mock(spec=_RealUserModel)
    mock_user_instance.get_full_info.return_value = "ID: 123, Name: Jane Doe, Email: jane@example.com"
    mock_user_class.return_value = mock_user_instance
    mock_capitalize.return_value = "Jane Doe"

    # Execute
    result = create_and_format_user("jane doe", "jane@example.com", "123")

    # Assertions
    assert result == "Formatted: Jane Doe | ID: 123, Name: Jane Doe, Email: jane@example.com"
    mock_user_class.assert_called_once_with("jane doe", "jane@example.com", "123")
    mock_capitalize.assert_called_once_with("jane doe")
    mock_user_instance.get_full_info.assert_called_once()

@patch(f'{__name__}.capitalize_words')
@patch(f'{__name__}.UserModel')
def test_create_and_format_user_edge_cases(mock_user_class, mock_capitalize):
    # Setup mocks for empty/None inputs
    mock_user_instance = Mock(spec=_RealUserModel)
    mock_user_instance.get_full_info.return_value = "ID: None, Name: , Email: "
    mock_user_class.return_value = mock_user_instance
    mock_capitalize.return_value = ""

    # Execute with minimal data
    result = create_and_format_user("", "", None)

    # Assertions
    assert result == "Formatted:  | ID: None, Name: , Email: "
    mock_user_class.assert_called_once_with("", "", None)
    mock_capitalize.assert_called_once_with("")

@patch(f'{__name__}.UserModel')
def test_create_and_format_user_error(mock_user_class):
    # Setup mock to raise an exception during instantiation
    mock_user_class.side_effect = ValueError("Invalid email format")

    # Assert exception is propagated
    with pytest.raises(ValueError, match="Invalid email format"):
        create_and_format_user("John", "invalid-email")

    mock_user_class.assert_called_once()