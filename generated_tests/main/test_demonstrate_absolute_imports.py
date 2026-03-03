import pytest
from unittest.mock import Mock, patch

# Define placeholders for the global names used in the function under test
# so that they can be patched on the test module.
add = None
subtract = None
multiply = None
divide = None
math_utils_module = None
utils = None
capitalize_words = None
reverse_string = None
count_words = None

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
    mock_cap_words, mock_reverse, mock_count, capsys
):
    # Setup mocks with realistic test data
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

    # Assertions for direct functions
    mock_add.assert_called_once_with(5, 3)
    mock_subtract.assert_called_once_with(10, 4)
    mock_multiply.assert_called_once_with(6, 7)
    mock_divide.assert_called_once_with(20, 4)
    
    # Assertions for module/package level
    mock_math_utils_module.add.assert_called_once_with(2, 2)
    mock_utils.add.assert_called_once_with(1, 1)
    mock_utils.capitalize_words.assert_called_once_with('hello world')
    
    # Assertions for string utils
    mock_cap_words.assert_called_once_with('python is great')
    mock_reverse.assert_called_once_with('hello')
    mock_count.assert_called_once_with('this is a test')

    # Verify output contains mocked values
    captured = capsys.readouterr()
    assert "add(5, 3) = 8.0" in captured.out
    assert "reverse_string('hello') = olleh" in captured.out

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
    mock_cap_words, mock_reverse, mock_count, capsys
):
    # Setup mocks with edge case values (zeros, empty strings)
    mock_add.return_value = 0.0
    mock_subtract.return_value = -1.0
    mock_multiply.return_value = 0.0
    mock_divide.return_value = 0.0
    mock_math_utils_module.add.return_value = 0.0
    mock_utils.add.return_value = 0.0
    mock_utils.capitalize_words.return_value = ""
    mock_cap_words.return_value = ""
    mock_reverse.return_value = ""
    mock_count.return_value = 0

    demonstrate_absolute_imports()

    captured = capsys.readouterr()
    assert "add(5, 3) = 0.0" in captured.out
    assert "count_words('this is a test') = 0" in captured.out
    assert "capitalize_words('python is great') = " in captured.out

@patch(f"{__name__}.count_words")
@patch(f"{__name__}.reverse_string")
@patch(f"{__name__}.capitalize_words")
@patch(f"{__name__}.utils")
@patch(f"{__name__}.math_utils_module")
@patch(f"{__name__}.divide")
@patch(f"{__name__}.multiply")
@patch(f"{__name__}.subtract")
@patch(f"{__name__}.add")
def test_demonstrate_absolute_imports_error(
    mock_add, mock_subtract, mock_multiply, mock_divide, 
    mock_math_utils_module, mock_utils, 
    mock_cap_words, mock_reverse, mock_count
):
    # Setup a mock to raise an exception
    # Since the function doesn't handle exceptions, it should propagate
    mock_add.side_effect = ValueError("Invalid input")

    with pytest.raises(ValueError) as excinfo:
        demonstrate_absolute_imports()
    
    assert str(excinfo.value) == "Invalid input"
    
    # Verify execution stopped at the error and subsequent mocks weren't called
    mock_subtract.assert_not_called()
    mock_utils.add.assert_not_called()
    mock_count.assert_not_called()