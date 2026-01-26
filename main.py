"""
Main Script
===========

This script demonstrates various import patterns in Python:
- Absolute imports
- Package imports
- Class imports
- Function imports
- Method imports
"""

# ============================================================================
# ABSOLUTE IMPORTS - Importing from packages using full paths
# ============================================================================

# Import specific functions from a module
from utils.math_utils import add, subtract, multiply, divide

# Import specific functions from another module
from utils.string_utils import capitalize_words, reverse_string, count_words

# Import a class from a module
from utils.data_processor import DataProcessor

# Import classes from models package
from models.base_model import BaseModel
from models.user_model import UserModel

# Import entire module
import utils.math_utils as math_utils_module

# Import entire package (using __init__.py exports)
import utils
import models


def demonstrate_absolute_imports():
    """Demonstrate absolute import patterns."""
    print("=" * 60)
    print("ABSOLUTE IMPORTS")
    print("=" * 60)
    
    # Using directly imported functions
    print(f"\n1. Direct function imports:")
    print(f"   add(5, 3) = {add(5, 3)}")
    print(f"   subtract(10, 4) = {subtract(10, 4)}")
    print(f"   multiply(6, 7) = {multiply(6, 7)}")
    print(f"   divide(20, 4) = {divide(20, 4)}")
    
    # Using module-level imports
    print(f"\n2. Module-level imports:")
    print(f"   math_utils_module.add(2, 2) = {math_utils_module.add(2, 2)}")
    
    # Using package-level imports (from __init__.py)
    print(f"\n3. Package-level imports:")
    print(f"   utils.add(1, 1) = {utils.add(1, 1)}")
    print(f"   utils.capitalize_words('hello world') = {utils.capitalize_words('hello world')}")
    
    # Using string utilities
    print(f"\n4. String utilities:")
    print(f"   capitalize_words('python is great') = {capitalize_words('python is great')}")
    print(f"   reverse_string('hello') = {reverse_string('hello')}")
    print(f"   count_words('this is a test') = {count_words('this is a test')}")


def demonstrate_class_imports():
    """Demonstrate class import patterns."""
    print("\n" + "=" * 60)
    print("CLASS IMPORTS")
    print("=" * 60)
    
    # Using imported DataProcessor class
    print(f"\n1. DataProcessor class:")
    processor = DataProcessor("test data")
    print(f"   processor.process() = {processor.process()}")
    print(f"   processor.transform('uppercase') = {processor.transform('uppercase')}")
    print(f"   processor.validate() = {processor.validate()}")
    
    # Using imported BaseModel class
    print(f"\n2. BaseModel class:")
    base = BaseModel("base-123")
    print(f"   base.id = {base.id}")
    print(f"   base.to_dict() = {base.to_dict()}")
    
    # Using imported UserModel class (inherits from BaseModel)
    print(f"\n3. UserModel class (inherits from BaseModel):")
    user = UserModel("John Doe", "john@example.com", "user-456")
    print(f"   user.name = {user.name}")
    print(f"   user.email = {user.email}")
    print(f"   user.get_full_info() = {user.get_full_info()}")
    print(f"   user.to_dict() = {user.to_dict()}")


def demonstrate_method_imports():
    """Demonstrate method usage from imported classes."""
    print("\n" + "=" * 60)
    print("METHOD IMPORTS")
    print("=" * 60)
    
    # Create instances and use their methods
    processor = DataProcessor([1, 2, 3, 4, 5])
    print(f"\n1. DataProcessor methods:")
    print(f"   process() method: {processor.process()}")
    print(f"   transform() method: {processor.transform('sort')}")
    print(f"   validate() method: {processor.validate()}")
    
    user = UserModel("Jane Smith", "jane@example.com")
    print(f"\n2. UserModel methods (including inherited):")
    print(f"   save() method (inherited): {user.save()}")
    print(f"   to_dict() method (overridden): {user.to_dict()}")
    print(f"   get_full_info() method: {user.get_full_info()}")


def main():
    """Main function to run all demonstrations."""
    print("\n" + "=" * 60)
    print("PYTHON IMPORT PATTERNS DEMONSTRATION")
    print("=" * 60)
    
    demonstrate_absolute_imports()
    demonstrate_class_imports()
    demonstrate_method_imports()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
