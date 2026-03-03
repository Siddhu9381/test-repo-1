import pytest
from unittest.mock import patch, Mock
from utils.data_processor import DataProcessor
from models.user_model import UserModel

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
    # Setup DataProcessor mock
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = "processed_results"
    mock_processor.transform.return_value = "transformed_results"
    mock_processor.validate.return_value = True
    
    # Setup UserModel mock
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.save.return_value = "record_id_123"
    mock_user.to_dict.return_value = {"name": "Jane Smith", "email": "jane@example.com"}
    mock_user.get_full_info.return_value = "Jane Smith <jane@example.com>"
    
    # Execute
    demonstrate_method_imports()
    
    # Verify DataProcessor interactions
    mock_dp_class.assert_called_once_with([1, 2, 3, 4, 5])
    mock_processor.process.assert_called_once()
    mock_processor.transform.assert_called_once_with('sort')
    mock_processor.validate.assert_called_once()
    
    # Verify UserModel interactions
    mock_um_class.assert_called_once()
    mock_user.save.assert_called_once()
    mock_user.to_dict.assert_called_once()
    mock_user.get_full_info.assert_called_once()

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_edge_cases(mock_dp_class, mock_um_class):
    # Setup mocks with empty/boundary return values
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = None
    mock_processor.transform.return_value = []
    mock_processor.validate.return_value = False
    
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.save.return_value = False
    mock_user.to_dict.return_value = {}
    mock_user.get_full_info.return_value = ""
    
    # Execute
    demonstrate_method_imports()
    
    # Assertions on edge values
    assert mock_processor.validate.return_value is False
    assert mock_user.to_dict.return_value == {}
    mock_processor.transform.assert_called_with('sort')
    mock_dp_class.assert_called_once()

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_method_imports_error(mock_dp_class, mock_um_class):
    # Setup DataProcessor to raise an exception during processing
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.side_effect = ValueError("Invalid data format")
    
    # Execute and Assert exception propagation
    with pytest.raises(ValueError, match="Invalid data format"):
        demonstrate_method_imports()
    
    # Verify that execution stopped before UserModel creation
    mock_processor.process.assert_called_once()
    mock_um_class.assert_not_called()
    mock_processor.transform.assert_not_called()