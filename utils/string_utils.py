"""
String Utilities Module
========================

This module provides string manipulation utility functions.

Functions:
    capitalize_words(text): Capitalize first letter of each word
    reverse_string(text): Reverse a string
    count_words(text): Count words in a string
"""


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text: Input string
    
    Returns:
        String with capitalized words
    
    Example:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return ' '.join(word.capitalize() for word in text.split())


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: Input string
    
    Returns:
        Reversed string
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def count_words(text: str) -> int:
    """
    Count the number of words in a string.
    
    Args:
        text: Input string
    
    Returns:
        Number of words
    
    Example:
        >>> count_words("hello world")
        2
    """
    return len(text.split())
