import pytest
from unittest.mock import patch, Mock
from utils.data_processor import DataProcessor
from models.user_model import UserModel

# Save real class references for spec usage before patching
_RealDataProcessor = DataProcessor
_RealUserModel = UserModel

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

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_success(mock_dp_class, mock_um_class):
    """Test the happy path where all methods return expected data."""
    # Setup DataProcessor mock
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = [10, 20, 30]
    mock_processor.transform.return_value = [5, 4, 3, 2, 1]
    mock_processor.validate.return_value = True

    # Setup UserModel mock
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.save.return_value = "Success"
    mock_user.to_dict.return_value = {"name": "Jane Smith", "email": "jane@example.com"}
    mock_user.get_full_info.return_value = "Jane Smith (jane@example.com)"

    # Execute
    demonstrate_method_imports()

    # Assertions for DataProcessor
    mock_dp_class.assert_called_once_with([1, 2, 3, 4, 5])
    mock_processor.process.assert_called_once()
    mock_processor.transform.assert_called_once_with('sort')
    mock_processor.validate.assert_called_once()

    # Assertions for UserModel
    mock_um_class.assert_called_once_with("Jane Smith", "jane@example.com")
    mock_user.save.assert_called_once()
    mock_user.to_dict.assert_called_once()
    mock_user.get_full_info.assert_called_once()

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_edge_cases(mock_dp_class, mock_um_class):
    """Test behavior with empty return values and boolean boundaries."""
    # Setup DataProcessor mock with empty/False values
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = []
    mock_processor.transform.return_value = None
    mock_processor.validate.return_value = False

    # Setup UserModel mock with empty strings/dicts
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.save.return_value = ""
    mock_user.to_dict.return_value = {}
    mock_user.get_full_info.return_value = ""

    # Execute - should handle empty/None values gracefully as it only prints them
    demonstrate_method_imports()

    # Verify calls still occurred
    assert mock_processor.validate.called
    assert mock_user.to_dict.called
    assert mock_user.to_dict.return_value == {}

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_error(mock_dp_class, mock_um_class):
    """Test error handling when a method raises an exception."""
    # Setup DataProcessor to work normally
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = "ok"
    mock_processor.transform.return_value = "ok"
    mock_processor.validate.return_value = True

    # Setup UserModel to raise an exception on save()
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.save.side_effect = Exception("Database Connection Failed")

    # Assert that the exception propagates since the function has no try/except
    with pytest.raises(Exception) as excinfo:
        demonstrate_method_imports()
    
    assert "Database Connection Failed" in str(excinfo.value)
    
    # Verify that DataProcessor methods were called before the exception
    mock_processor.process.assert_called_once()
    # Verify save was the point of failure
    mock_user.save.assert_called_once()
    # verify subsequent calls did not happen
    mock_user.to_dict.assert_not_called()