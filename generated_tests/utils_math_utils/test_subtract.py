import pytest
from unittest.mock import Mock, patch

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
    """Test the happy path with normal integer and float inputs."""
    # Test with integers
    assert subtract(10, 5) == 5.0
    # Test with floats
    assert subtract(10.5, 2.5) == 8.0
    # Test with negative results
    assert subtract(5, 10) == -5.0
    # Test with negative inputs
    assert subtract(-5, -3) == -2.0

def test_subtract_edge_cases():
    """Test boundaries and edge cases like zero and large numbers."""
    # Test subtracting zero
    assert subtract(5.0, 0.0) == 5.0
    # Test subtracting from zero
    assert subtract(0.0, 5.0) == -5.0
    # Test subtracting identical numbers
    assert subtract(123.456, 123.456) == 0.0
    # Test very large numbers
    assert subtract(1e18, 1.0) == 1e18 - 1.0
    # Test very small numbers
    assert subtract(1e-10, 1e-11) == 9e-11

def test_subtract_error():
    """Test exception handling when invalid types are provided."""
    # Test with None values
    with pytest.raises(TypeError):
        subtract(None, 5)
    
    with pytest.raises(TypeError):
        subtract(5, None)
        
    # Test with string values
    with pytest.raises(TypeError):
        subtract("10", 5)
        
    with pytest.raises(TypeError):
        subtract(10, "5")
        
    # Test with complex objects
    with pytest.raises(TypeError):
        subtract([1], {2})