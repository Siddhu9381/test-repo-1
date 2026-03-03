import pytest
from unittest.mock import patch, Mock

# Dependency stubs for patching
def add(a, b): pass
def multiply(a, b): pass
def divide(a, b): pass

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
    """Happy path with normal inputs, exercising all loops and calculations."""
    # Setup mock behavior for input [10, 20]
    # Summing loop: add(0, 10) -> 10.0, then add(10.0, 20) -> 30.0
    mock_add.side_effect = [10.0, 30.0]
    # Average calculation: divide(30.0, 2)
    mock_divide.return_value = 15.0
    # Product loop: multiply(1, 10) -> 10.0, then multiply(10.0, 20) -> 200.0
    mock_multiply.side_effect = [10.0, 200.0]
    
    input_data = [10, 20]
    result = calculate_statistics(input_data)
    
    expected_result = {
        'sum': 30.0,
        'average': 15.0,
        'product': 200.0,
        'count': 2
    }
    
    assert result == expected_result
    assert mock_add.call_count == 2
    mock_divide.assert_called_once_with(30.0, 2)
    assert mock_multiply.call_count == 2

def test_calculate_statistics_edge_cases():
    """Test empty values and boundaries where the early return path is triggered."""
    # Empty list case
    empty_list_result = calculate_statistics([])
    assert empty_list_result == {'sum': 0, 'average': 0, 'product': 0}
    
    # None input case
    none_result = calculate_statistics(None)
    assert none_result == {'sum': 0, 'average': 0, 'product': 0}

@patch(f'{__name__}.add')
@patch(f'{__name__}.divide')
def test_calculate_statistics_error(mock_divide, mock_add):
    """Test exception handling and error propagation from dependencies."""
    # Simulate valid sum but an error during division
    mock_add.return_value = 5.0
    mock_divide.side_effect = ZeroDivisionError("Mocked division error")
    
    with pytest.raises(ZeroDivisionError, match="Mocked division error"):
        calculate_statistics([5])
    
    # Verify that the function attempted the calculation before failing
    mock_add.assert_called()
    mock_divide.assert_called_once()