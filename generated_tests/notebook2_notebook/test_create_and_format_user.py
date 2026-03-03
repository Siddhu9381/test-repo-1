import pytest
from unittest.mock import Mock, patch
from models.user_model import UserModel
from utils.string_utils import capitalize_words

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

# Save reference for spec before patching
_RealUserModel = UserModel

@patch(f"{__name__}.capitalize_words")
@patch(f"{__name__}.UserModel")
def test_create_and_format_user_success(MockUserModel, MockCapitalizeWords):
    # Setup
    mock_user = Mock(spec=_RealUserModel)
    mock_user.get_full_info.return_value = "Name: Jane Doe, Email: jane@example.com, ID: 555"
    MockUserModel.return_value = mock_user
    MockCapitalizeWords.return_value = "Jane Doe"

    # Execute
    result = create_and_format_user("jane doe", "jane@example.com", "555")

    # Assert
    expected = "Formatted: Jane Doe | Name: Jane Doe, Email: jane@example.com, ID: 555"
    assert result == expected
    MockUserModel.assert_called_once_with("jane doe", "jane@example.com", "555")
    MockCapitalizeWords.assert_called_once_with("jane doe")
    mock_user.get_full_info.assert_called_once()

@patch(f"{__name__}.capitalize_words")
@patch(f"{__name__}.UserModel")
def test_create_and_format_user_edge_cases(MockUserModel, MockCapitalizeWords):
    # Setup: Test with empty strings and None user_id
    mock_user = Mock(spec=_RealUserModel)
    mock_user.get_full_info.return_value = "Name: , Email: none@test.com, ID: None"
    MockUserModel.return_value = mock_user
    MockCapitalizeWords.return_value = ""

    # Execute
    result = create_and_format_user("", "none@test.com", None)

    # Assert
    assert "Formatted:  |" in result
    assert "ID: None" in result
    MockUserModel.assert_called_once_with("", "none@test.com", None)
    MockCapitalizeWords.assert_called_once_with("")

@patch(f"{__name__}.capitalize_words")
@patch(f"{__name__}.UserModel")
def test_create_and_format_user_error(MockUserModel, MockCapitalizeWords):
    # Setup: Simulate an exception during the formatting process
    mock_user = Mock(spec=_RealUserModel)
    MockUserModel.return_value = mock_user
    MockCapitalizeWords.return_value = "Error User"
    
    # Simulate get_full_info raising an unexpected error
    mock_user.get_full_info.side_effect = RuntimeError("Database connection failed")

    # Execute & Assert
    with pytest.raises(RuntimeError, match="Database connection failed"):
        create_and_format_user("Error User", "error@test.com", "999")
    
    # Verify the flow reached the point of failure
    MockUserModel.assert_called_once()
    MockCapitalizeWords.assert_called_once()
    mock_user.get_full_info.assert_called_once()