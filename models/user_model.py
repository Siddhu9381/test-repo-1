"""
User Model Module
=================

This module provides a UserModel class that inherits from BaseModel.

Classes:
    UserModel: User model class
"""

# Relative import from the same package
from .base_model import BaseModel


class UserModel(BaseModel):
    """
    User model class representing a user.
    
    Inherits from BaseModel and adds user-specific functionality.
    
    Attributes:
        id: Unique identifier (inherited)
        created_at: Creation timestamp (inherited)
        name: User's name
        email: User's email
    
    Methods:
        save(): Save the user (inherited)
        delete(): Delete the user (inherited)
        to_dict(): Convert user to dictionary (overridden)
        get_full_info(): Get full user information
    """
    
    def __init__(self, name: str, email: str, id: str = None):
        """
        Initialize UserModel.
        
        Args:
            name: User's name
            email: User's email
            id: Unique identifier (optional)
        """
        # Call parent class constructor
        super().__init__(id)
        self.name = name
        self.email = email
    
    def to_dict(self) -> dict:
        """
        Convert user to dictionary.
        
        Overrides parent class method to include user-specific fields.
        
        Returns:
            Dictionary representation of the user
        """
        base_dict = super().to_dict()
        base_dict.update({
            'name': self.name,
            'email': self.email
        })
        return base_dict
    
    def get_full_info(self) -> str:
        """
        Get full user information as a formatted string.
        
        Returns:
            Formatted string with user information
        """
        return f"User: {self.name} ({self.email}) - ID: {self.id}"
