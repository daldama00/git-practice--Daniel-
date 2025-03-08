# Bug Fixes

## 1. `divide_numbers(a, b)`
- **Bug**: The function didn't handle division by zero.
- **How Identified**: Running the test `divide_numbers(10, 0)` caused a crash.
- **Fix Applied**: Added a check to raise `ZeroDivisionError` when `b == 0`.

## 2. `reverse_string(s)`
- **Bug**: The function didn't handle non-string inputs.
- **How Identified**: Running the test `reverse_string(123)` made this crash.
- **Fix Applied**: Added a check to raise `TypeError` if `s` is not a string.

## 3. `get_list_element(lst, index)`
- **Bug**: The function didn't handle out-of-range indices properly and returned "Not found" instead.
- **How Identified**: Running the test `get_list_element([1, 2, 3], 3)` returned `"Not found"` instead of raising an exception.
- **Fix Applied**: Changed the boundary check to raise an `IndexError` if the index is out of bounds.

