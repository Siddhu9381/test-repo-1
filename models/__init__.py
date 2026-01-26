"""
Models Package
==============

This package contains model classes for data modeling.

Exports:
    - BaseModel: Base model class
    - UserModel: User model class
"""

# Absolute imports from within the package
from models.base_model import BaseModel
from models.user_model import UserModel

# Package-level exports
__all__ = [
    'BaseModel',
    'UserModel',
]
