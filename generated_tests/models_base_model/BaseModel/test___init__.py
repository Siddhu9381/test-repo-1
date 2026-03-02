import pytest
from unittest.mock import patch, Mock
import datetime

_RealDatetimeClass = datetime.datetime

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
def test_init_success(mock_datetime_module):
    # Setup mock for the datetime class and its now() method
    mock_datetime_class = Mock(spec=_RealDatetimeClass)
    mock_datetime_module.datetime = mock_datetime_class
    mock_now_val = _RealDatetimeClass(2023, 1, 1, 12, 0, 0)
    mock_datetime_class.now.return_value = mock_now_val
    
    test_id = "model-123"
    model = BaseModel(id=test_id)
    
    assert model.id == test_id
    assert model.created_at == mock_now_val
    mock_datetime_class.now.assert_called_once()

@patch(f'{__name__}.datetime')
def test_init_edge_cases(mock_datetime_module):
    # Setup mock for the datetime class and its now() method
    mock_datetime_class = Mock(spec=_RealDatetimeClass)
    mock_datetime_module.datetime = mock_datetime_class
    mock_now_val = _RealDatetimeClass(2023, 5, 20, 10, 30, 0)
    mock_datetime_class.now.return_value = mock_now_val
    
    # Case 1: id is None
    model_none = BaseModel(id=None)
    assert model_none.id is None
    assert model_none.created_at == mock_now_val
    
    # Case 2: id is an empty string
    model_empty = BaseModel(id="")
    assert model_empty.id == ""
    assert model_empty.created_at == mock_now_val

@patch(f'{__name__}.datetime')
def test_init_error(mock_datetime_module):
    # Setup mock to raise an exception when datetime.now() is called
    mock_datetime_class = Mock(spec=_RealDatetimeClass)
    mock_datetime_module.datetime = mock_datetime_class
    error_message = "System clock failure"
    mock_datetime_class.now.side_effect = RuntimeError(error_message)
    
    with pytest.raises(RuntimeError) as exc_info:
        BaseModel(id="error-test")
    
    assert str(exc_info.value) == error_message
    mock_datetime_class.now.assert_called_once()