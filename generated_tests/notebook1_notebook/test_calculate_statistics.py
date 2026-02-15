import pytest
from unittest.mock import patch, Mock, call

def add(a, b):
    pass

def multiply(a, b):
    pass

def divide(a, b):
    pass

def calculate_statistics(numbers):
    """
    Calculate basic statistics for a list of numbers.
    
    This function demonstrates using multiple imported functions together.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Dictionary with sum, average, and product
    """
    if not numbers:
        return {'sum': 0, 'average': 0, 'product': 0}
    
    # Calculate sum using imported add function
    total_sum = 0
    for num in numbers:
        total_sum = add(total_sum, num)
    
    # Calculate average
    count = len(numbers)
    average = divide(total_sum, count)
    
    # Calculate product using imported multiply function
    product = 1
    for num in numbers:
        product = multiply(product, num)
    
    return {
        'sum': total_sum,
        'average': average,
        'product': product,
        'count': count
    }

@patch(f'{__name__}.multiply')
@patch(f'{__name__}.divide')
@patch(f'{__name__}.add')
def test_calculate_statistics_success(mock_add, mock_divide, mock_multiply):
    """Test the happy path with a standard list of numbers."""
    # Setup mocks for input [10, 20]
    # Sum: add(0, 10) -> 10, add(10, 20) -> 30
    mock_add.side_effect = [10, 30]
    # Average: divide(30, 2) -> 15
    mock_divide.return_value = 15
    # Product: multiply(1, 10) -> 10, multiply(10, 20) -> 200
    mock_multiply.side_effect = [10, 200]
    
    test_input = [10, 20]
    expected_output = {
        'sum': 30,
        'average': 15,
        'product': 200,
        'count': 2
    }
    
    result = calculate_statistics(test_input)
    
    # Assertions
    assert result == expected_output
    assert mock_add.call_count == 2
    mock_add.assert_has_calls([call(0, 10), call(10, 20)])
    mock_divide.assert_called_once_with(30, 2)
    assert mock_multiply.call_count == 2
    mock_multiply.assert_has_calls([call(1, 10), call(10, 20)])

@patch(f'{__name__}.multiply')
@patch(f'{__name__}.divide')
@patch(f'{__name__}.add')
def test_calculate_statistics_edge_cases(mock_add, mock_divide, mock_multiply):
    """Test empty input, None, and single-item lists."""
    # Case 1: Empty list
    assert calculate_statistics([]) == {'sum': 0, 'average': 0, 'product': 0}
    
    # Case 2: None input (should be caught by 'if not numbers')
    assert calculate_statistics(None) == {'sum': 0, 'average': 0, 'product': 0}
    
    # Case 3: Single item list [5]
    mock_add.return_value = 5
    mock_divide.return_value = 5.0
    mock_multiply.return_value = 5
    
    result = calculate_statistics([5])
    
    assert result == {'sum': 5, 'average': 5.0, 'product': 5, 'count': 1}
    mock_add.assert_called_with(0, 5)
    mock_divide.assert_called_with(5, 1)
    mock_multiply.assert_called_with(1, 5)

@patch(f'{__name__}.multiply')
@patch(f'{__name__}.divide')
@patch(f'{__name__}.add')
def test_calculate_statistics_error(mock_add, mock_divide, mock_multiply):
    """Test error propagation and invalid types."""
    # Case 1: Dependency raises an internal exception (e.g., division error)
    mock_add.return_value = 10
    mock_divide.side_effect = ZeroDivisionError("Math error")
    
    with pytest.raises(ZeroDivisionError, match="Math error"):
        calculate_statistics([10])
    
    # Case 2: Input that is not a list/iterable and not falsy
    # This will trigger a TypeError during the for-loop iteration
    with pytest.raises(TypeError):
        calculate_statistics(12345)
        
    # Case 3: Dependency raises TypeError due to bad data
    mock_add.side_effect = TypeError("Unsupported operand types")
    with pytest.raises(TypeError, match="Unsupported operand types"):
        calculate_statistics(["not", "a", "number"])