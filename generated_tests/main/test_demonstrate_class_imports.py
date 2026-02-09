import pytest
from unittest.mock import Mock, patch

# Note: For the unit tests to run and patch correctly, the function 
# demonstrate_class_imports must be defined in the scope where the tests are run (or imported).
# We define it here assuming it resides in the '__main__' module for patching purposes.

def demonstrate_class_imports():
    """Demonstrate class import patterns."""
    
    # Placeholder classes needed only for definition scope if run locally
    try:
        DataProcessor
        BaseModel
        UserModel
    except NameError:
        # These dummy definitions are overwritten by mocks during testing, 
        # but required to prevent NameError during function definition scope analysis.
        class DataProcessor:
            def __init__(self, data): pass
            def process(self): return None
            def transform(self, transformation: str): return None
            def validate(self) -> bool: return False
        class BaseModel:
            def __init__(self, id: str): self.id = id
            def to_dict(self) -> dict: return {"id": self.id}
        class UserModel(BaseModel):
            def __init__(self, name: str, email: str, id: str): super().__init__(id); self.name = name; self.email = email
            def get_full_info(self) -> str: return f"{self.name}, {self.email}"
    
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


TARGET_PATH = '__main__'

# --- Mock Data Setup ---
MOCK_PROC_PROCESS_S = "Data Successfully Processed"
MOCK_PROC_TRANSFORM_S = "TRANSFORMED_STRING"
MOCK_PROC_VALIDATE_S = True
MOCK_BASE_ID_S = "base-123-mocked"
MOCK_BASE_DICT_S = {"id": "base-123-mocked", "status": "active"}
MOCK_USER_NAME_S = "John Mock"
MOCK_USER_EMAIL_S = "john.mock@test.com"
MOCK_USER_FULL_INFO_S = "John Mock (ID: user-456) is ready."
MOCK_USER_DICT_S = {"name": "John Mock", "email": "john.mock@test.com", "id": "user-456"}


@patch(f'{TARGET_PATH}.UserModel')
@patch(f'{TARGET_PATH}.BaseModel')
@patch(f'{TARGET_PATH}.DataProcessor')
def test_demonstrate_class_imports_success(
    MockDataProcessor, MockBaseModel, MockUserModel, capsys
):
    # Setup DataProcessor instance mock
    mock_processor_instance = MockDataProcessor.return_value
    mock_processor_instance.process.return_value = MOCK_PROC_PROCESS_S
    mock_processor_instance.transform.return_value = MOCK_PROC_TRANSFORM_S
    mock_processor_instance.validate.return_value = MOCK_PROC_VALIDATE_S

    # Setup BaseModel instance mock
    mock_base_instance = MockBaseModel.return_value
    # Note: attribute assignment must happen directly on the mock instance
    type(mock_base_instance).id = property(lambda self: MOCK_BASE_ID_S)
    mock_base_instance.to_dict.return_value = MOCK_BASE_DICT_S

    # Setup UserModel instance mock
    mock_user_instance = MockUserModel.return_value
    type(mock_user_instance).name = property(lambda self: MOCK_USER_NAME_S)
    type(mock_user_instance).email = property(lambda self: MOCK_USER_EMAIL_S)
    mock_user_instance.get_full_info.return_value = MOCK_USER_FULL_INFO_S
    mock_user_instance.to_dict.return_value = MOCK_USER_DICT_S

    demonstrate_class_imports()

    # Verify constructor calls (Inputs are fixed by the function logic)
    MockDataProcessor.assert_called_once_with("test data")
    MockBaseModel.assert_called_once_with("base-123")
    MockUserModel.assert_called_once_with("John Doe", "john@example.com", "user-456")

    # Verify method calls
    mock_processor_instance.process.assert_called_once()
    mock_processor_instance.transform.assert_called_once_with('uppercase')
    mock_user_instance.get_full_info.assert_called_once()
    
    # Verify output logging
    captured = capsys.readouterr()
    output = captured.out

    assert f"processor.process() = {MOCK_PROC_PROCESS_S}" in output
    assert f"base.id = {MOCK_BASE_ID_S}" in output
    assert f"user.get_full_info() = {MOCK_USER_FULL_INFO_S}" in output


@patch(f'{TARGET_PATH}.UserModel')
@patch(f'{TARGET_PATH}.BaseModel')
@patch(f'{TARGET_PATH}.DataProcessor')
def test_demonstrate_class_imports_edge_cases(
    MockDataProcessor, MockBaseModel, MockUserModel, capsys
):
    # Setup DataProcessor instance mock with edge cases
    mock_processor_instance = MockDataProcessor.return_value
    mock_processor_instance.process.return_value = ""
    mock_processor_instance.transform.return_value = None
    mock_processor_instance.validate.return_value = False

    # Setup BaseModel instance mock with edge cases
    mock_base_instance = MockBaseModel.return_value
    type(mock_base_instance).id = property(lambda self: "")
    mock_base_instance.to_dict.return_value = {}

    # Setup UserModel instance mock with edge cases
    mock_user_instance = MockUserModel.return_value
    type(mock_user_instance).name = property(lambda self: "")
    type(mock_user_instance).email = property(lambda self: "")
    mock_user_instance.get_full_info.return_value = "Minimal Info"
    mock_user_instance.to_dict.return_value = {}

    demonstrate_class_imports()

    # Verify instantiation still happens
    MockDataProcessor.assert_called_once()
    MockBaseModel.assert_called_once()
    MockUserModel.assert_called_once()
    
    # Verify output logging reflects edge values (empty strings, None, False, empty dicts)
    captured = capsys.readouterr()
    output = captured.out

    assert f"processor.process() = " in output # Empty string output
    assert f"processor.transform('uppercase') = None" in output
    assert f"processor.validate() = False" in output
    assert f"base.id = " in output # Empty string output
    assert f"base.to_dict() = {{}}" in output
    assert f"user.name = " in output # Empty string output
    assert f"user.get_full_info() = Minimal Info" in output
    assert f"user.to_dict() = {{}}" in output


@patch(f'{TARGET_PATH}.UserModel')
@patch(f'{TARGET_PATH}.BaseModel')
@patch(f'{TARGET_PATH}.DataProcessor')
def test_demonstrate_class_imports_error(
    MockDataProcessor, MockBaseModel, MockUserModel, capsys
):
    ERROR_MESSAGE = "DataProcessor failed during execution."

    # Scenario: DataProcessor instantiation succeeds, but the first method call fails
    mock_processor_instance = MockDataProcessor.return_value
    mock_processor_instance.process.side_effect = RuntimeError(ERROR_MESSAGE)

    # Execution should halt at processor.process()
    with pytest.raises(RuntimeError) as excinfo:
        demonstrate_class_imports()

    # Check exception details
    assert ERROR_MESSAGE in str(excinfo.value)
    
    # Check that DataProcessor was initialized and process was called once
    MockDataProcessor.assert_called_once_with("test data")
    mock_processor_instance.process.assert_called_once()
    
    # Check that subsequent classes (BaseModel, UserModel) were never called
    MockBaseModel.assert_not_called()
    MockUserModel.assert_not_called()
    
    # Check output to ensure execution stopped early
    captured = capsys.readouterr()
    output = captured.out
    
    assert "1. DataProcessor class:" in output
    assert "2. BaseModel class:" not in output