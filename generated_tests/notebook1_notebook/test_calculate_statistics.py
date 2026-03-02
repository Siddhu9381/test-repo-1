import pytest
from unittest.mock import patch, Mock

# Dependencies for mocking
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
    """Test happy path with multiple numbers."""
    # Setup mock behaviors for input [2, 4]
    # Sum: add(0, 2) -> 2, add(2, 4) -> 6
    mock_add.side_effect = [2, 6]
    # Average: divide(6, 2) -> 3.0
    mock_divide.return_value = 3.0
    # Product: multiply(1, 2) -> 2, multiply(2, 4) -> 8
    mock_multiply.side_effect = [2, 8]
    
    numbers = [2, 4]
    result = calculate_statistics(numbers)
    
    expected = {
        'sum': 6,
        'average': 3.0,
        'product': 8,
        'count': 2
    }
    
    assert result == expected
    assert mock_add.call_count == 2
    mock_divide.assert_called_once_with(6, 2)
    assert mock_multiply.call_count == 2

@patch(f'{__name__}.multiply')
@patch(f'{__name__}.divide')
@patch(f'{__name__}.add')
def test_calculate_statistics_edge_cases(mock_add, mock_divide, mock_multiply):
    """Test empty list and single item boundaries."""
    # Case 1: Empty list (Branch coverage: not numbers)
    empty_result = calculate_statistics([])
    assert empty_result == {'sum': 0, 'average': 0, 'product': 0}
    mock_add.assert_not_called()
    
    # Case 2: Single item list
    mock_add.return_value = 10
    mock_divide.return_value = 10.0
    mock_multiply.return_value = 10
    
    single_result = calculate_statistics([10])
    assert single_result == {
        'sum': 10,
        'average': 10.0,
        'product': 10,
        'count': 1
    }
    mock_add.assert_called_with(0, 10)
    mock_divide.assert_called_with(10, 1)
    mock_multiply.assert_called_with(1, 10)

@patch(f'{__name__}.add')
def test_calculate_statistics_error(mock_add):
    """Test exception handling when external dependencies raise errors."""
    # Simulate a TypeError if invalid data is passed and add fails
    mock_add.side_effect = TypeError("Unsupported operand types")
    
    with pytest.raises(TypeError, match="Unsupported operand types"):
        calculate_statistics(["invalid", "input"])
    
    # Verify the function stopped at the first dependency failure
    assert mock_add.called_once()