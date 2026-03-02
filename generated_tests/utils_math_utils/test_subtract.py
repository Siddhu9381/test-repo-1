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
    """Test the happy path with standard float and integer inputs."""
    # Test positive subtraction
    assert subtract(10.0, 5.0) == 5.0
    # Test negative results
    assert subtract(5.0, 10.0) == -5.0
    # Test subtraction with negative numbers
    assert subtract(-1.0, -1.0) == 0.0
    # Test integer promotion to float
    assert subtract(10, 5) == 5.0
    assert isinstance(subtract(10, 5), (float, int))

def test_subtract_edge_cases():
    """Test boundary conditions, zeros, and floating point limits."""
    # Test zeros
    assert subtract(0.0, 0.0) == 0.0
    assert subtract(0.0, 5.0) == -5.0
    # Test large numbers
    assert subtract(1e18, 1.0) == 1e18 - 1.0
    # Test infinity behavior
    inf = float('inf')
    assert subtract(inf, 1.0) == inf
    assert subtract(1.0, inf) == float('-inf')
    # Test precision with pytest.approx
    assert subtract(0.3, 0.1) == pytest.approx(0.2)

def test_subtract_error():
    """Test error handling for invalid input types."""
    # Test with strings
    with pytest.raises(TypeError):
        subtract("5", 3)
    # Test with None values
    with pytest.raises(TypeError):
        subtract(5.0, None)
    # Test with complex data structures
    with pytest.raises(TypeError):
        subtract([10.0], 5.0)