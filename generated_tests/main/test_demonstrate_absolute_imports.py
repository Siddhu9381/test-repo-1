import pytest
from unittest.mock import Mock, patch
import sys
import io

# --- Function Under Test Definition ---
# This function relies on external names (add, utils, etc.) which must be mocked
# using @patch targeting __main__ if defined in the same script.

def demonstrate_absolute_imports():
    """Demonstrate absolute import patterns."""
    
    # NOTE: These names (add, subtract, utils, etc.) are assumed to be imported 
    # into the scope where this function is defined.
    
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


# Helper list for patching order (reversed order of decorators in Python)
PATCH_TARGETS = [
    '__main__.count_words',
    '__main__.reverse_string',
    '__main__.capitalize_words',
    '__main__.utils',
    '__main__.math_utils_module',
    '__main__.divide',
    '__main__.multiply',
    '__main__.subtract',
    '__main__.add',
]

# Apply patches using a context manager for cleaner parameter passing
def apply_patches(func):
    for target in PATCH_TARGETS:
        func = patch(target)(func)
    return func

@apply_patches
def test_demonstrate_absolute_imports_success(
    mock_add, mock_subtract, mock_multiply, mock_divide, mock_math_utils_module, mock_utils, 
    mock_capitalize_words_str, mock_reverse_string, mock_count_words, capsys
):
    # Setup return values (Happy Path)
    add_ret, sub_ret, mul_ret, div_ret = 8.0, 6.0, 42.0, 5.0
    math_add_ret = 4.0
    utils_add_ret, utils_cap_ret = 2.0, 'Hello World (Util)'
    cap_ret, rev_ret, count_ret = 'Python Is Great (String)', 'olleh', 4

    mock_add.return_value = add_ret
    mock_subtract.return_value = sub_ret
    mock_multiply.return_value = mul_ret
    mock_divide.return_value = div_ret
    
    mock_math_utils_module.add.return_value = math_add_ret
    
    mock_utils.add.return_value = utils_add_ret
    mock_utils.capitalize_words.return_value = utils_cap_ret
    
    mock_capitalize_words_str.return_value = cap_ret
    mock_reverse_string.return_value = rev_ret
    mock_count_words.return_value = count_ret

    # Execute
    demonstrate_absolute_imports()
    
    # Capture output
    captured = capsys.readouterr()
    output = captured.out

    # Assertions on calls
    mock_add.assert_called_once_with(5, 3)
    mock_divide.assert_called_once_with(20, 4)
    mock_math_utils_module.add.assert_called_once_with(2, 2)
    mock_utils.capitalize_words.assert_called_once_with('hello world')
    mock_count_words.assert_called_once_with('this is a test')
    
    # Assertions on output content
    assert f"add(5, 3) = {add_ret}" in output
    assert f"divide(20, 4) = {div_ret}" in output
    assert f"math_utils_module.add(2, 2) = {math_add_ret}" in output
    assert f"utils.capitalize_words('hello world') = {utils_cap_ret}" in output
    assert f"reverse_string('hello') = {rev_ret}" in output


@apply_patches
def test_demonstrate_absolute_imports_edge_cases(
    mock_add, mock_subtract, mock_multiply, mock_divide, mock_math_utils_module, mock_utils, 
    mock_capitalize_words_str, mock_reverse_string, mock_count_words, capsys
):
    # Setup edge case return values
    
    # Math results near zero or negative
    mock_add.return_value = 0.0
    mock_subtract.return_value = -10.0
    mock_multiply.return_value = 0.0
    mock_divide.return_value = 0.0
    mock_math_utils_module.add.return_value = 1.0
    mock_utils.add.return_value = 0.0
    
    # String results: Empty strings or zero counts
    mock_utils.capitalize_words.return_value = ""
    mock_capitalize_words_str.return_value = ""
    mock_reverse_string.return_value = "a"
    mock_count_words.return_value = 0

    # Execute
    demonstrate_absolute_imports()
    
    captured = capsys.readouterr()
    output = captured.out

    # Assertions on calls (ensure arguments are correct)
    mock_add.assert_called_once_with(5, 3)
    mock_utils.capitalize_words.assert_called_once_with('hello world')
    
    # Assertions on output content (Checking edge case results)
    assert "add(5, 3) = 0.0" in output
    assert "subtract(10, 4) = -10.0" in output
    assert "divide(20, 4) = 0.0" in output
    # Check for empty strings in output
    assert "utils.capitalize_words('hello world') = " in output
    assert "capitalize_words('python is great') = " in output
    assert "count_words('this is a test') = 0" in output


@apply_patches
def test_demonstrate_absolute_imports_error(
    mock_add, mock_subtract, mock_multiply, mock_divide, mock_math_utils_module, mock_utils, 
    mock_capitalize_words_str, mock_reverse_string, mock_count_words
):
    
    # Setup mocks for calls that happen BEFORE the error
    mock_add.return_value = 8.0
    mock_subtract.return_value = 6.0
    mock_multiply.return_value = 42.0
    
    # Make 'divide' raise an error, stopping execution in Section 1
    mock_divide.side_effect = ZeroDivisionError("Mocked Division Failure")

    # Execution should raise the exception
    with pytest.raises(ZeroDivisionError) as excinfo:
        demonstrate_absolute_imports()
        
    assert "Mocked Division Failure" in str(excinfo.value)

    # Assert that prior calls succeeded
    mock_add.assert_called_once()
    mock_subtract.assert_called_once()
    mock_multiply.assert_called_once()
    mock_divide.assert_called_once_with(20, 4)
    
    # Assert that subsequent calls were NOT made (e.g., Section 2 and 3)
    mock_math_utils_module.add.assert_not_called()
    mock_utils.add.assert_not_called()
    mock_count_words.assert_not_called()