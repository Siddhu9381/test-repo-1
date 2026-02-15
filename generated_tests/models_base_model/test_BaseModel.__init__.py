import pytest
from unittest.mock import patch, MagicMock
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

@patch(f'{__name__}.datetime')
def test_init_success(mock_datetime):
    # Setup mock return value for datetime.now()
    fixed_now = datetime(2023, 10, 27, 12, 0, 0)
    mock_datetime.now.return_value = fixed_now
    
    test_id = "user-12345"
    model = BaseModel(id=test_id)
    
    # Assertions
    assert model.id == test_id
    assert model.created_at == fixed_now
    mock_datetime.now.assert_called_once()

@patch(f'{__name__}.datetime')
def test_init_edge_cases(mock_datetime):
    # Setup mock return value
    fixed_now = datetime(2023, 10, 27, 12, 0, 0)
    mock_datetime.now.return_value = fixed_now
    
    # Test with None (default behavior)
    model_none = BaseModel(id=None)
    assert model_none.id is None
    assert model_none.created_at == fixed_now
    
    # Test with empty string
    model_empty = BaseModel(id="")
    assert model_empty.id == ""
    assert model_empty.created_at == fixed_now
    
    assert mock_datetime.now.call_count == 2

@patch(f'{__name__}.datetime')
def test_init_error(mock_datetime):
    # Simulate an error during datetime.now() call
    mock_datetime.now.side_effect = RuntimeError("System clock failure")
    
    # Assert that the exception propagates correctly
    with pytest.raises(RuntimeError) as exc_info:
        BaseModel(id="error-id")
    
    assert str(exc_info.value) == "System clock failure"
    mock_datetime.now.assert_called_once()