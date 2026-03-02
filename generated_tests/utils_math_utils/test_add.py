import pytest
from unittest.mock import patch, Mock
import math

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
    """Happy path with normal inputs."""
    # Test positive floats
    assert add(10.5, 4.5) == 15.0
    # Test negative floats
    assert add(-1.0, -2.5) == -3.5
    # Test mixed integers and floats
    assert add(5, 3.0) == 8.0
    # Test floating point precision using approx
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_add_edge_cases():
    """None, empty values, boundaries."""
    # Test zeros
    assert add(0.0, 0.0) == 0.0
    # Test infinity
    assert add(float('inf'), 1.0) == float('inf')
    assert add(float('-inf'), -1.0) == float('-inf')
    # Test NaN result (inf + -inf)
    assert math.isnan(add(float('inf'), float('-inf')))
    # Test very large numbers resulting in overflow to infinity
    assert add(1e308, 1e308) == float('inf')

def test_add_error():
    """Exception handling and error paths."""
    # Test passing None (should raise TypeError)
    with pytest.raises(TypeError):
        add(None, 5.0)
    # Test passing strings
    with pytest.raises(TypeError):
        add("5", 3.0)
    # Test passing incompatible types like lists
    with pytest.raises(TypeError):
        add(1.0, [1, 2, 3])
    # Test missing arguments
    with pytest.raises(TypeError):
        add(1.0)