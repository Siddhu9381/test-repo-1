import pytest
from unittest.mock import patch, Mock
import math

def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b
    
    Example:
        >>> subtract(5, 3)
        2
    """
    return a - b

def test_subtract_success():
    """Test subtract with standard integer and float inputs, including negative results."""
    # Test basic positive float subtraction
    assert subtract(10.5, 5.5) == 5.0
    # Test subtraction resulting in a negative number
    assert subtract(5.0, 10.0) == -5.0
    # Test subtraction with negative numbers
    assert subtract(-1.0, -5.0) == 4.0
    # Test subtraction with mixed integer and float types
    assert subtract(20, 5.5) == 14.5
    # Test subtraction resulting in zero
    assert subtract(1.23, 1.23) == 0.0

def test_subtract_edge_cases():
    """Test subtract with zeros, infinities, and large values."""
    # Test zero boundaries
    assert subtract(0.0, 0.0) == 0.0
    # Test subtraction with infinity
    assert subtract(float('inf'), 1.0) == float('inf')
    assert subtract(1.0, float('inf')) == float('-inf')
    assert subtract(float('inf'), float('-inf')) == float('inf')
    # Test NaN case: infinity minus infinity is undefined
    assert math.isnan(subtract(float('inf'), float('inf')))
    # Test very large numbers (float precision limits)
    assert subtract(1e18, 1.0) == 1e18 - 1.0

def test_subtract_error():
    """Test subtract with invalid types to ensure TypeErrors are raised."""
    # Test with string as first argument
    with pytest.raises(TypeError):
        subtract("10", 5.0)
    # Test with None as second argument
    with pytest.raises(TypeError):
        subtract(10.0, None)
    # Test with complex data structures
    with pytest.raises(TypeError):
        subtract([10.0], 5.0)
    # Test with dictionaries
    with pytest.raises(TypeError):
        subtract(10.0, {"value": 5.0})