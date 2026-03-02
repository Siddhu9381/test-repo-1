import pytest
from unittest.mock import patch, Mock
from models.base_model import BaseModel
from utils.data_processor import DataProcessor
from models.user_model import UserModel

def demonstrate_class_imports():
    """Demonstrate class import patterns."""
    print("\n" + "=" * 60)
    print("CLASS IMPORTS")
    print("=" * 60)
    
    # Using imported DataProcessor class
    print(f"\n1. DataProcessor class:")
    processor = DataProcessor("test data")
    print(f"   processor.process() = {processor.process()}")
    print(f"   processor.transform('uppercase') = {processor.transform('uppercase')}")
    print(f"   processor.validate() = {processor.validate()}")
    
    # Using imported BaseModel class
    print(f"\n2. BaseModel class:")
    base = BaseModel("base-123")
    print(f"   base.id = {base.id}")
    print(f"   base.to_dict() = {base.to_dict()}")
    
    # Using imported UserModel class (inherits from BaseModel)
    print(f"\n3. UserModel class (inherits from BaseModel):")
    user = UserModel("John Doe", "john@example.com", "user-456")
    print(f"   user.name = {user.name}")
    print(f"   user.email = {user.email}")
    print(f"   user.get_full_info() = {user.get_full_info()}")
    print(f"   user.to_dict() = {user.to_dict()}")

_RealDataProcessor = DataProcessor
_RealBaseModel = BaseModel
_RealUserModel = UserModel

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.BaseModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_class_imports_success(mock_dp_class, mock_bm_class, mock_um_class):
    """Test the happy path where all classes and methods behave normally."""
    # Setup DataProcessor mock
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = "processed_result"
    mock_processor.transform.return_value = "TRANSFORMED_RESULT"
    mock_processor.validate.return_value = True

    # Setup BaseModel mock
    mock_base = Mock(spec=_RealBaseModel)
    mock_bm_class.return_value = mock_base
    mock_base.id = "base-123"
    mock_base.to_dict.return_value = {"id": "base-123", "type": "base"}

    # Setup UserModel mock
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.name = "John Doe"
    mock_user.email = "john@example.com"
    mock_user.get_full_info.return_value = "John Doe <john@example.com>"
    mock_user.to_dict.return_value = {"id": "user-456", "name": "John Doe"}

    # Execute
    demonstrate_class_imports()

    # Assertions for DataProcessor
    mock_dp_class.assert_called_once_with("test data")
    mock_processor.process.assert_called_once()
    mock_processor.transform.assert_called_once_with('uppercase')
    mock_processor.validate.assert_called_once()

    # Assertions for BaseModel
    mock_bm_class.assert_called_once_with("base-123")
    mock_base.to_dict.assert_called_once()

    # Assertions for UserModel
    mock_um_class.assert_called_once_with("John Doe", "john@example.com", "user-456")
    mock_user.get_full_info.assert_called_once()
    mock_user.to_dict.assert_called_once()

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.BaseModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_class_imports_edge_cases(mock_dp_class, mock_bm_class, mock_um_class):
    """Test edge cases such as empty strings, None values, and empty dictionaries."""
    # DataProcessor returns empty/None values
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.return_value = ""
    mock_processor.transform.return_value = None
    mock_processor.validate.return_value = False

    # BaseModel with empty ID and dict
    mock_base = Mock(spec=_RealBaseModel)
    mock_bm_class.return_value = mock_base
    mock_base.id = ""
    mock_base.to_dict.return_value = {}

    # UserModel with special characters and empty info
    mock_user = Mock(spec=_RealUserModel)
    mock_um_class.return_value = mock_user
    mock_user.name = "N/A"
    mock_user.email = ""
    mock_user.get_full_info.return_value = ""
    mock_user.to_dict.return_value = {}

    # Execute should not raise exceptions despite empty/None returns
    demonstrate_class_imports()

    assert mock_dp_class.called
    assert mock_bm_class.called
    assert mock_um_class.called

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.BaseModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_class_imports_error(mock_dp_class, mock_bm_class, mock_um_class):
    """Test error handling when dependencies raise exceptions."""
    # Setup DataProcessor to raise an error during processing
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_dp_class.return_value = mock_processor
    mock_processor.process.side_effect = RuntimeError("Processing failed")

    # The function does not have a try-except block, so the exception should propagate
    with pytest.raises(RuntimeError, match="Processing failed"):
        demonstrate_class_imports()

    # Verify that the processor was instantiated before the crash
    mock_dp_class.assert_called_once_with("test data")
    # Verify that subsequent code (BaseModel/UserModel) was not reached
    mock_bm_class.assert_not_called()
    mock_um_class.assert_not_called()