"""
Math Utilities Module
=====================

This module provides mathematical utility functions for basic arithmetic operations.

Functions:
    add(a, b): Add two numbers
    subtract(a, b): Subtract b from a
    multiply(a, b): Multiply two numbers
    divide(a, b): Divide a by b
"""


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
