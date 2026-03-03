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
    """Happy path with normal inputs."""
    # Test simple integer division resulting in float
    assert divide(15.0, 3.0) == 5.0
    # Test division with larger numbers
    assert divide(100.0, 10.0) == 10.0
    # Test that the return type is float
    result = divide(20.0, 5.0)
    assert isinstance(result, float)
    assert result == 4.0

def test_divide_edge_cases():
    """None, empty values, boundaries, and negative numbers."""
    # Test division by negative numbers
    assert divide(10.0, -2.0) == -5.0
    assert divide(-10.0, 2.0) == -5.0
    assert divide(-10.0, -2.0) == 5.0
    # Test dividend as zero
    assert divide(0.0, 5.0) == 0.0
    # Test result that is a repeating decimal
    assert pytest.approx(divide(1.0, 3.0)) == 0.3333333333
    # Test small float values
    assert divide(0.1, 0.1) == 1.0

def test_divide_error():
    """Exception handling and error paths."""
    # Test the specific branch where b == 0
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(10.0, 0.0)
    
    # Verify the exception message matches the implementation
    assert str(excinfo.value) == "Cannot divide by zero"
    
    # Ensure the exception is raised regardless of the dividend
    with pytest.raises(ZeroDivisionError):
        divide(-5.0, 0.0)
    with pytest.raises(ZeroDivisionError):
        divide(0.0, 0.0)