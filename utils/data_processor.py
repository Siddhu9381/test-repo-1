"""
Data Processor Module
=====================

This module provides a DataProcessor class for processing data.

Classes:
    DataProcessor: Class for processing and transforming data
"""


class DataProcessor:
    """
    A class for processing and transforming data.
    
    Attributes:
        data: The data being processed
    
    Methods:
        process(): Process the data
        transform(): Transform the data
        validate(): Validate the data
    """
    
    def __init__(self, data):
        """
        Initialize DataProcessor with data.
        
        Args:
            data: Data to be processed
        """
        self.data = data
    
    def process(self):
        """
        Process the data.
        
        Returns:
            Processed data
        """
        return f"Processed: {self.data}"
    
    def transform(self, transformation: str):
        """
        Transform the data.
        
        Args:
            transformation: Type of transformation to apply
        
        Returns:
            Transformed data
        """
        return f"Transformed ({transformation}): {self.data}"
    
    def validate(self) -> bool:
        """
        Validate the data.
        
        Returns:
            True if data is valid, False otherwise
        """
        return self.data is not None and len(str(self.data)) > 0
