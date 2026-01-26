"""
Base Model Module
=================

This module provides a base model class that other models can inherit from.

Classes:
    BaseModel: Base class for all models
"""


class BaseModel:
    """
    Base model class providing common functionality for all models.
    
    Attributes:
        id: Unique identifier
        created_at: Creation timestamp
    
    Methods:
        save(): Save the model
        delete(): Delete the model
        to_dict(): Convert model to dictionary
    """
    
    def __init__(self, id: str = None):
        """
        Initialize BaseModel.
        
        Args:
            id: Unique identifier for the model
        """
        self.id = id
        from datetime import datetime
        self.created_at = datetime.now()
    
    def save(self):
        """
        Save the model.
        
        Returns:
            True if saved successfully
        """
        return True
    
    def delete(self):
        """
        Delete the model.
        
        Returns:
            True if deleted successfully
        """
        return True
    
    def to_dict(self) -> dict:
        """
        Convert model to dictionary.
        
        Returns:
            Dictionary representation of the model
        """
        return {
            'id': self.id,
            'created_at': str(self.created_at)
        }
