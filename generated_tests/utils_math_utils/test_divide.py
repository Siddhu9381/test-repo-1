import pytest
from unittest.mock import patch, Mock

def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Quotient of a and b
    
    Raises:
        ZeroDivisionError: If b is zero
    
    Example:
        >>> divide(15, 3)
        5.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_divide_success():
    """Test happy path with standard float and integer inputs."""
    # Test simple integer division resulting in float
    assert divide(15, 3) == 5.0
    # Test division with float inputs
    assert divide(10.5, 2.0) == 5.25
    # Test division with negative dividend
    assert divide(-20.0, 5.0) == -4.0
    # Verify return type is always float
    assert isinstance(divide(10, 2), float)

def test_divide_edge_cases():
    """Test boundaries including zero dividend, negative divisors, and large values."""
    # Dividend is zero
    assert divide(0.0, 10.0) == 0.0
    # Both values are negative
    assert divide(-10.0, -2.0) == 5.0
    # Large number handling
    assert divide(1e10, 10.0) == 1e9
    # Small decimal precision
    assert divide(0.1, 0.5) == 0.2
    # Divisor is a very small non-zero float
    assert divide(1.0, 0.000001) == 1000000.0

def test_divide_error():
    """Test exception handling for division by zero."""
    # Ensure ZeroDivisionError is raised with correct message
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(10.0, 0.0)
    
    assert str(exc_info.value) == "Cannot divide by zero"
    
    # Ensure it also raises for integer zero
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)