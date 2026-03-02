import pytest
from unittest.mock import patch, Mock

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    
    Example:
        >>> multiply(5, 3)
        15
    """
    return a * b

def test_multiply_success():
    """Happy path with normal inputs."""
    # Test integer-like floats
    assert multiply(5.0, 3.0) == 15.0
    # Test decimal floats
    assert multiply(2.5, 4.0) == 10.0
    # Test floating point precision using pytest.approx
    assert multiply(0.1, 0.2) == pytest.approx(0.02)
    # Test large numbers
    assert multiply(1e6, 1e6) == 1e12

def test_multiply_edge_cases():
    """None, empty values, boundaries."""
    # Test multiplication by zero
    assert multiply(0.0, 100.0) == 0.0
    assert multiply(55.5, 0.0) == 0.0
    assert multiply(0.0, 0.0) == 0.0
    # Test negative numbers
    assert multiply(-5.0, 3.0) == -15.0
    assert multiply(5.0, -3.0) == -15.0
    assert multiply(-5.0, -3.0) == 15.0
    # Test identity property
    assert multiply(1.0, 99.9) == 99.9
    assert multiply(99.9, 1.0) == 99.9

def test_multiply_error():
    """Exception handling and error paths."""
    # Test with None values (should raise TypeError)
    with pytest.raises(TypeError):
        multiply(None, 5.0)
    
    # Test with incompatible types (strings)
    with pytest.raises(TypeError):
        multiply("2", 5.0)
    
    # Test with incompatible types (lists)
    with pytest.raises(TypeError):
        multiply(5.0, [1, 2, 3])

    # Test with missing arguments
    with pytest.raises(TypeError):
        multiply(5.0)