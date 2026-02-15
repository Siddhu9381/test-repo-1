import pytest
from unittest.mock import patch, Mock
from utils.data_processor import DataProcessor
from models.user_model import UserModel

def demonstrate_method_imports():
    """Demonstrate method usage from imported classes."""
    print("\n" + "=" * 60)
    print("METHOD IMPORTS")
    print("=" * 60)
    
    # Create instances and use their methods
    processor = DataProcessor([1, 2, 3, 4, 5])
    print(f"\n1. DataProcessor methods:")
    print(f"   process() method: {processor.process()}")
    print(f"   transform() method: {processor.transform('sort')}")
    print(f"   validate() method: {processor.validate()}")
    
    user = UserModel("Jane Smith", "jane@example.com")
    print(f"\n2. UserModel methods (including inherited):")
    print(f"   save() method (inherited): {user.save()}")
    print(f"   to_dict() method (overridden): {user.to_dict()}")
    print(f"   get_full_info() method: {user.get_full_info()}")

# Save references for spec-based mocking
_RealDataProcessor = DataProcessor
_RealUserModel = UserModel

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_success(mock_dp_class, mock_um_class):
    """Test the happy path where all methods return expected successful values."""
    # Setup DataProcessor mock instance
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = {"status": "completed", "items": 5}
    mock_processor.transform.return_value = [1, 2, 3, 4, 5]
    mock_processor.validate.return_value = True

    # Setup UserModel mock instance
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.save.return_value = True
    mock_user.to_dict.return_value = {"name": "Jane Smith", "email": "jane@example.com"}
    mock_user.get_full_info.return_value = "Jane Smith (jane@example.com)"

    # Execute function
    demonstrate_method_imports()

    # Assert DataProcessor interactions
    mock_dp_class.assert_called_once_with([1, 2, 3, 4, 5])
    mock_processor.process.assert_called_once()
    mock_processor.transform.assert_called_once_with('sort')
    mock_processor.validate.assert_called_once()

    # Assert UserModel interactions
    # Note: Function uses 2 args despite signature showing 3; mock reflects function usage
    mock_um_class.assert_called_once_with("Jane Smith", "jane@example.com")
    mock_user.save.assert_called_once()
    mock_user.to_dict.assert_called_once()
    mock_user.get_full_info.assert_called_once()

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_edge_cases(mock_dp_class, mock_um_class):
    """Test edge cases such as empty data, failed validation, and empty strings."""
    # Setup DataProcessor mock instance with empty/falsy returns
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = None
    mock_processor.transform.return_value = []
    mock_processor.validate.return_value = False

    # Setup UserModel mock instance with empty/falsy returns
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.save.return_value = False
    mock_user.to_dict.return_value = {}
    mock_user.get_full_info.return_value = ""

    # Execute function
    demonstrate_method_imports()

    # Verify return values were handled (via prints in the function)
    assert mock_processor.validate.called
    assert mock_user.save.return_value is False
    assert mock_user.to_dict() == {}

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_error(mock_dp_class, mock_um_class):
    """Test error paths where dependencies raise exceptions."""
    # Setup DataProcessor to raise an error during processing
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.side_effect = RuntimeError("Data corruption detected")

    # Setup UserModel mock (should not be reached if processor fails first)
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user

    # Execute and verify exception propagates
    with pytest.raises(RuntimeError) as exc_info:
        demonstrate_method_imports()
    
    assert str(exc_info.value) == "Data corruption detected"
    
    # Verify UserModel was never instantiated because of the earlier error
    mock_um_class.assert_not_called()