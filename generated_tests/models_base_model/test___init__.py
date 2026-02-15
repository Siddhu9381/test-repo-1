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

_RealDateTime = datetime

@patch(f'{__name__}.datetime')
def test_init_success(mock_datetime_class):
    # Setup
    mock_now = _RealDateTime(2023, 10, 27, 12, 0, 0)
    mock_datetime_class.now.return_value = mock_now
    test_id = "user-123"

    # Execute
    model = BaseModel(id=test_id)

    # Assert
    assert model.id == test_id
    assert model.created_at == mock_now
    mock_datetime_class.now.assert_called_once()

@patch(f'{__name__}.datetime')
def test_init_edge_cases(mock_datetime_class):
    # Setup
    mock_now = _RealDateTime(2023, 10, 27, 12, 0, 0)
    mock_datetime_class.now.return_value = mock_now

    # Case 1: ID is None
    model_none = BaseModel(id=None)
    assert model_none.id is None
    assert model_none.created_at == mock_now

    # Case 2: ID is an empty string
    model_empty = BaseModel(id="")
    assert model_empty.id == ""
    assert model_empty.created_at == mock_now

@patch(f'{__name__}.datetime')
def test_init_error(mock_datetime_class):
    # Setup: Mock datetime.now to raise an exception
    mock_datetime_class.now.side_effect = RuntimeError("System clock failure")
    
    # Execute & Assert
    with pytest.raises(RuntimeError) as exc_info:
        BaseModel(id="error-test")
    
    assert str(exc_info.value) == "System clock failure"
    mock_datetime_class.now.assert_called_once()