import pytest
from unittest.mock import patch, Mock
from datetime import datetime

class BaseModel:
    def __init__(self, id: str = None):
        """
        Initialize BaseModel.
        
        Args:
            id: Unique identifier for the model
        """
        self.id = id
        from datetime import datetime
        self.created_at = datetime.now()

@patch('datetime.datetime')
def test_init_success(mock_datetime):
    # Happy path: Test initialization with a valid string ID
    fixed_now = datetime(2023, 10, 27, 12, 0, 0)
    mock_datetime.now.return_value = fixed_now
    test_id = "uuid-12345"
    
    model = BaseModel(id=test_id)
    
    assert model.id == test_id
    assert model.created_at == fixed_now
    mock_datetime.now.assert_called_once()

@patch('datetime.datetime')
def test_init_edge_cases(mock_datetime):
    # Edge cases: Test initialization with None and empty values
    fixed_now = datetime(2023, 10, 27, 12, 0, 0)
    mock_datetime.now.return_value = fixed_now
    
    # Case 1: ID is None
    model_none = BaseModel(id=None)
    assert model_none.id is None
    assert model_none.created_at == fixed_now
    
    # Case 2: ID is an empty string
    model_empty = BaseModel(id="")
    assert model_empty.id == ""
    assert model_empty.created_at == fixed_now

@patch('datetime.datetime')
def test_init_error(mock_datetime):
    # Error path: Test how the function handles an exception from an external dependency
    # Since the code doesn't catch exceptions, we verify it propagates them
    mock_datetime.now.side_effect = RuntimeError("System clock failure")
    
    with pytest.raises(RuntimeError) as exc_info:
        BaseModel(id="error-test-id")
    
    assert "System clock failure" in str(exc_info.value)