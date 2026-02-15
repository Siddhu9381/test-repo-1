import pytest
from unittest.mock import patch, Mock
from models.base_model import BaseModel
from models.user_model import UserModel
from utils.data_processor import DataProcessor

# Save references before patching for use with spec
_RealBaseModel = BaseModel
_RealUserModel = UserModel
_RealDataProcessor = DataProcessor

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

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.BaseModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_class_imports_success(mock_dp_class, mock_bm_class, mock_um_class):
    # Setup DataProcessor mock
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_processor.process.return_value = "Success Processed"
    mock_processor.transform.return_value = "SUCCESS TRANSFORMED"
    mock_processor.validate.return_value = True
    mock_dp_class.return_value = mock_processor

    # Setup BaseModel mock
    mock_base = Mock(spec=_RealBaseModel)
    mock_base.id = "base-123"
    mock_base.to_dict.return_value = {"id": "base-123", "type": "base"}
    mock_bm_class.return_value = mock_base

    # Setup UserModel mock
    mock_user = Mock(spec=_RealUserModel)
    mock_user.name = "John Doe"
    mock_user.email = "john@example.com"
    mock_user.get_full_info.return_value = "John Doe <john@example.com>"
    mock_user.to_dict.return_value = {"id": "user-456", "name": "John Doe", "email": "john@example.com"}
    mock_um_class.return_value = mock_user

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
    # Setup mocks with empty/boundary values
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_processor.process.return_value = ""
    mock_processor.transform.return_value = ""
    mock_processor.validate.return_value = False
    mock_dp_class.return_value = mock_processor

    mock_base = Mock(spec=_RealBaseModel)
    mock_base.id = ""
    mock_base.to_dict.return_value = {}
    mock_bm_class.return_value = mock_base

    mock_user = Mock(spec=_RealUserModel)
    mock_user.name = ""
    mock_user.email = ""
    mock_user.get_full_info.return_value = "Unknown"
    mock_user.to_dict.return_value = {}
    mock_um_class.return_value = mock_user

    # Execute - should handle empty return strings/dicts gracefully in print statements
    demonstrate_class_imports()

    # Verify calls still occurred with expected hardcoded inputs
    mock_dp_class.assert_called_with("test data")
    mock_bm_class.assert_called_with("base-123")
    mock_um_class.assert_called_with("John Doe", "john@example.com", "user-456")

@patch(f'{__name__}.DataProcessor')
def test_demonstrate_class_imports_error(mock_dp_class):
    # Setup mock to raise an exception during processing
    mock_processor = Mock(spec=_RealDataProcessor)
    mock_processor.process.side_effect = RuntimeError("Processing failed")
    mock_dp_class.return_value = mock_processor

    # Since the function does not have try-except blocks, the error should propagate
    with pytest.raises(RuntimeError) as excinfo:
        demonstrate_class_imports()
    
    assert str(excinfo.value) == "Processing failed"
    mock_dp_class.assert_called_once()
    mock_processor.process.assert_called_once()