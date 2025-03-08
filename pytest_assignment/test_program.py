import pytest
from program import divide_numbers, reverse_string, get_list_element

# Test for divide_numbers
def test_divide_numbers_normal():
    assert divide_numbers(10, 2) == 5.00

def test_divide_numbers_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)

def test_divide_numbers_negative_divisor():
    assert divide_numbers(10, -2) == -5.00

# Test for reverse_string
def test_reverse_string_normal():
    assert reverse_string("Hello") == "OLLEh"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_non_string_input():
    with pytest.raises(TypeError):
        reverse_string(123)

# Test for get_list_element
def test_get_list_element_normal():
    assert get_list_element([1, 2, 3], 1) == 2

def test_get_list_element_out_of_range():
    assert get_list_element([1, 2, 3], 3) == "Not found"

def test_get_list_element_negative_index():
    assert get_list_element([1, 2, 3], -1) == 3
