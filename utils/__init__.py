"""
Utils Package
=============

This package contains utility modules for mathematical operations,
string manipulation, and data processing.

Exports:
    - math_utils: Mathematical utility functions
    - string_utils: String manipulation functions
    - data_processor: Data processing class
"""

# Absolute imports from within the package
from utils.math_utils import add, subtract, multiply, divide
from utils.string_utils import capitalize_words, reverse_string, count_words
from utils.data_processor import DataProcessor

# Package-level exports
__all__ = [
    'add',
    'subtract',
    'multiply',
    'divide',
    'capitalize_words',
    'reverse_string',
    'count_words',
    'DataProcessor',
]
