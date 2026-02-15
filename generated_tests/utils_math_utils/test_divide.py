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
    """Test happy path with normal floating point and integer inputs."""
    # Test simple integer division resulting in whole float
    assert divide(15.0, 3.0) == 5.0
    # Test division resulting in a decimal
    assert divide(10.0, 4.0) == 2.5
    # Test division with negative numbers
    assert divide(-10.0, 2.0) == -5.0
    assert divide(-20.0, -5.0) == 4.0
    # Test division with large numbers
    assert divide(1000000.0, 10.0) == 100000.0

def test_divide_edge_cases():
    """Test boundary conditions, zero dividend, and precision scenarios."""
    # Test zero as the dividend (should return 0.0)
    assert divide(0.0, 5.0) == 0.0
    assert divide(0.0, -1.0) == 0.0
    # Test very small numbers
    assert divide(1e-10, 1.0) == 1e-10
    # Test floating point precision (using approx for safety)
    assert divide(1.0, 3.0) == pytest.approx(0.3333333333333333)
    # Test division by 1 and -1
    assert divide(5.5, 1.0) == 5.5
    assert divide(5.5, -1.0) == -5.5

def test_divide_error():
    """Test the ZeroDivisionError exception path."""
    # Test that dividing by zero raises the specific ZeroDivisionError
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(10.0, 0.0)
    
    # Verify the error message matches the implementation
    assert str(exc_info.value) == "Cannot divide by zero"
    
    # Test with negative dividend and zero divisor
    with pytest.raises(ZeroDivisionError):
        divide(-5.0, 0)
    
    # Test with zero dividend and zero divisor
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)