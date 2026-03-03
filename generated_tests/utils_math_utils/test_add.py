import pytest
from unittest.mock import patch, Mock

def add(a: float, b: float) -> float:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    
    Example:
        >>> add(5, 3)
        8
    """
    return a + b

def test_add_success():
    """Happy path with normal inputs including positive, negative, and float values."""
    # Test with integers as floats
    assert add(5.0, 3.0) == 8.0
    # Test with negative numbers
    assert add(-10.5, 5.5) == -5.0
    # Test with decimals
    assert add(1.25, 0.75) == 2.0
    # Test docstring example
    assert add(5, 3) == 8

def test_add_edge_cases():
    """Boundaries, zero values, and floating point precision."""
    # Test zero boundaries
    assert add(0.0, 0.0) == 0.0
    assert add(0.0, -0.0) == 0.0
    # Test floating point precision using pytest.approx
    assert add(0.1, 0.2) == pytest.approx(0.3)
    # Test infinity boundaries
    assert add(float('inf'), 1.0) == float('inf')
    assert add(float('-inf'), -1.0) == float('-inf')
    # Test very large numbers (overflowing to inf)
    assert add(1e308, 1e308) == float('inf')

def test_add_error():
    """Exception handling and error paths for invalid types."""
    # Test None input
    with pytest.raises(TypeError):
        add(None, 5.0)
    # Test string input
    with pytest.raises(TypeError):
        add("10", 20.0)
    # Test list input
    with pytest.raises(TypeError):
        add(5.0, [1, 2, 3])
    # Test complex numbers (if logic dictates strictly float, though + works, the hint says float)
    with pytest.raises(TypeError):
        # This is a forced scenario where we expect float but get incompatible types
        add(5.0, "unsupported")