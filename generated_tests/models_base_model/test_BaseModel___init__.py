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

@patch("datetime.datetime")
def test_init_success(mock_datetime):
    # Happy path with normal inputs
    mock_now = datetime(2023, 1, 1, 12, 0, 0)
    mock_datetime.now.return_value = mock_now
    test_id = "test-unique-id-123"
    
    model = BaseModel(id=test_id)
    
    assert model.id == test_id
    assert model.created_at == mock_now
    mock_datetime.now.assert_called_once()

@patch("datetime.datetime")
def test_init_edge_cases(mock_datetime):
    # None, empty values, boundaries
    mock_now = datetime(2023, 1, 1, 12, 0, 0)
    mock_datetime.now.return_value = mock_now
    
    # Test with None id
    model_none = BaseModel(id=None)
    assert model_none.id is None
    assert model_none.created_at == mock_now
    
    # Test with empty string id
    model_empty = BaseModel(id="")
    assert model_empty.id == ""
    assert model_empty.created_at == mock_now
    
    assert mock_datetime.now.call_count == 2

@patch("datetime.datetime")
def test_init_error(mock_datetime):
    # Exception handling and error paths
    # Mocking datetime.now to raise an exception to test error handling
    mock_datetime.now.side_effect = RuntimeError("System clock failure")
    
    with pytest.raises(RuntimeError) as exc_info:
        BaseModel(id="error-id")
    
    assert str(exc_info.value) == "System clock failure"