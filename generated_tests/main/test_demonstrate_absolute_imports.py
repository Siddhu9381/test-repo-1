import pytest
from unittest.mock import patch, Mock

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

# Global placeholders for patching
add = None
subtract = None
multiply = None
divide = None
math_utils_module = None
utils = None
capitalize_words = None
reverse_string = None
count_words = None

@patch(f"{__name__}.count_words")
@patch(f"{__name__}.reverse_string")
@patch(f"{__name__}.capitalize_words")
@patch(f"{__name__}.utils")
@patch(f"{__name__}.math_utils_module")
@patch(f"{__name__}.divide")
@patch(f"{__name__}.multiply")
@patch(f"{__name__}.subtract")
@patch(f"{__name__}.add")
def test_demonstrate_absolute_imports_success(
    mock_add, mock_subtract, mock_multiply, mock_divide, 
    mock_math_utils_module, mock_utils, 
    mock_cap_words, mock_reverse, mock_count
):
    # Setup mock return values
    mock_add.return_value = 8.0
    mock_subtract.return_value = 6.0
    mock_multiply.return_value = 42.0
    mock_divide.return_value = 5.0
    
    mock_math_utils_module.add.return_value = 4.0
    
    mock_utils.add.return_value = 2.0
    mock_utils.capitalize_words.return_value = "Hello World"
    
    mock_cap_words.return_value = "Python Is Great"
    mock_reverse.return_value = "olleh"
    mock_count.return_value = 4

    # Execute function
    demonstrate_absolute_imports()

    # Assertions for direct imports
    mock_add.assert_called_once_with(5, 3)
    mock_subtract.assert_called_once_with(10, 4)
    mock_multiply.assert_called_once_with(6, 7)
    mock_divide.assert_called_once_with(20, 4)

    # Assertions for module/package level imports
    mock_math_utils_module.add.assert_called_once_with(2, 2)
    mock_utils.add.assert_called_once_with(1, 1)
    mock_utils.capitalize_words.assert_called_once_with('hello world')

    # Assertions for string utilities
    mock_cap_words.assert_called_once_with('python is great')
    mock_reverse.assert_called_once_with('hello')
    mock_count.assert_called_once_with('this is a test')

@patch(f"{__name__}.count_words")
@patch(f"{__name__}.reverse_string")
@patch(f"{__name__}.capitalize_words")
@patch(f"{__name__}.utils")
@patch(f"{__name__}.math_utils_module")
@patch(f"{__name__}.divide")
@patch(f"{__name__}.multiply")
@patch(f"{__name__}.subtract")
@patch(f"{__name__}.add")
def test_demonstrate_absolute_imports_edge_cases(
    mock_add, mock_subtract, mock_multiply, mock_divide, 
    mock_math_utils_module, mock_utils, 
    mock_cap_words, mock_reverse, mock_count
):
    # Setup edge case return values (zeros and empty strings)
    mock_add.return_value = 0.0
    mock_subtract.return_value = -1.0
    mock_multiply.return_value = 0.0
    mock_divide.return_value = float('inf')
    
    mock_math_utils_module.add.return_value = 0.0
    
    mock_utils.add.return_value = 0.0
    mock_utils.capitalize_words.return_value = ""
    
    mock_cap_words.return_value = ""
    mock_reverse.return_value = ""
    mock_count.return_value = 0

    # Execute function
    demonstrate_absolute_imports()

    # Verify calls were still made correctly despite edge case returns
    assert mock_count.called
    assert mock_cap_words.return_value == ""
    assert mock_add.return_value == 0.0

@patch(f"{__name__}.add")
def test_demonstrate_absolute_imports_error(mock_add):
    # Setup mock to raise an exception
    mock_add.side_effect = Exception("Imported function failed")

    # Verify that the exception propagates up
    with pytest.raises(Exception) as excinfo:
        demonstrate_absolute_imports()
    
    assert str(excinfo.value) == "Imported function failed"
    mock_add.assert_called_once()
    # Verify execution stopped at the first failing call (add)
    # Subsequent calls like subtract, multiply etc. would not happen if add raises