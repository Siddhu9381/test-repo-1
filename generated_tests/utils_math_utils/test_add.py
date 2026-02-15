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
    """Happy path with normal inputs."""
    # Test positive floats
    result_pos = add(10.5, 4.5)
    assert result_pos == 15.0, f"Expected 15.0, got {result_pos}"
    
    # Test negative floats
    result_neg = add(-5.0, -3.2)
    assert result_neg == -8.2, f"Expected -8.2, got {result_neg}"
    
    # Test mixed integers and floats
    result_mixed = add(-1.0, 1.0)
    assert result_mixed == 0.0, f"Expected 0.0, got {result_mixed}"

def test_add_edge_cases():
    """None, empty values, boundaries."""
    # Test with zero
    assert add(0.0, 0.0) == 0.0, "Adding zeros should return zero"
    
    # Test with very large floats
    large_val = 1.79e308
    assert add(large_val, 0.0) == 1.79e308
    
    # Test with infinity
    inf = float('inf')
    assert add(inf, 1.0) == inf, "Infinity plus a number should be infinity"
    
    # Test floating point precision using approx
    assert add(0.1, 0.2) == pytest.approx(0.3), "Floating point addition should handle precision"

def test_add_error():
    """Exception handling and error paths."""
    # Test with None values
    with pytest.raises(TypeError):
        add(None, 5.0)
        
    # Test with string types
    with pytest.raises(TypeError):
        add("5", 3.0)
        
    # Test with list types
    with pytest.raises(TypeError):
        add(10.0, [1, 2])
        
    # Test with missing arguments
    with pytest.raises(TypeError):
        add(5.0) # type: ignore