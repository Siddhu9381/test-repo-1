import pytest
from unittest.mock import patch, Mock

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

# Placeholder classes to satisfy the namespace for patching
class DataProcessor:
    def __init__(self, data): pass
    def process(self): pass
    def transform(self, transformation): pass
    def validate(self): pass

class BaseModel:
    def __init__(self, id): pass
    def to_dict(self): pass

class UserModel:
    def __init__(self, name, email, id): pass
    def to_dict(self): pass
    def get_full_info(self): pass

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.BaseModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_class_imports_success(mock_dp_class, mock_bm_class, mock_um_class):
    # Dependency: processor (instance of DataProcessor)
    mock_processor = Mock(spec=DataProcessor)
    mock_processor.process.return_value = "processed success"
    mock_processor.transform.return_value = "TRANSFORMED SUCCESS"
    mock_processor.validate.return_value = True
    mock_dp_class.return_value = mock_processor

    # Dependency: base (instance of BaseModel)
    mock_base = Mock(spec=BaseModel)
    mock_base.id = "base-123"
    mock_base.to_dict.return_value = {"id": "base-123", "type": "base"}
    mock_bm_class.return_value = mock_base

    # Dependency: user (instance of UserModel)
    mock_user = Mock(spec=UserModel)
    mock_user.name = "John Doe"
    mock_user.email = "john@example.com"
    mock_user.get_full_info.return_value = "John Doe <john@example.com>"
    mock_user.to_dict.return_value = {"id": "user-456", "name": "John Doe"}
    mock_um_class.return_value = mock_user

    # Execute function
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
    # Test with empty strings, None, and False values
    mock_processor = Mock(spec=DataProcessor)
    mock_processor.process.return_value = ""
    mock_processor.transform.return_value = None
    mock_processor.validate.return_value = False
    mock_dp_class.return_value = mock_processor

    mock_base = Mock(spec=BaseModel)
    mock_base.id = ""
    mock_base.to_dict.return_value = {}
    mock_bm_class.return_value = mock_base

    mock_user = Mock(spec=UserModel)
    mock_user.name = None
    mock_user.email = ""
    mock_user.get_full_info.return_value = ""
    mock_user.to_dict.return_value = {}
    mock_um_class.return_value = mock_user

    # Function should handle empty/None mock returns without crashing
    demonstrate_class_imports()

    assert mock_processor.validate.called
    assert mock_base.to_dict.called
    assert mock_user.get_full_info.called

@patch(f'{__name__}.UserModel')
@patch(f'{__name__}.BaseModel')
@patch(f'{__name__}.DataProcessor')
def test_demonstrate_class_imports_error(mock_dp_class, mock_bm_class, mock_um_class):
    # Simulate an error during DataProcessor instantiation
    mock_dp_class.side_effect = RuntimeError("Failed to initialize processor")

    with pytest.raises(RuntimeError, match="Failed to initialize processor"):
        demonstrate_class_imports()

    # Verify that first class was attempted and subsequent ones were not
    mock_dp_class.assert_called_once()
    mock_bm_class.assert_not_called()
    mock_um_class.assert_not_called()