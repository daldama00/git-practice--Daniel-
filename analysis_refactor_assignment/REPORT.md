# Static and Dynamic Code Analysis Report

## Static Analysis

**flake8**:
- Line 1: unused import `math`
- Line 2: unused import `random`

**pylint**:
- `slow_func` could be simplified
- `unused_function` never used

## Line Profiling

Bottleneck in:
- `expensive_op`: Took ~3s for 1000 calls

### Fix:
- Replaced loop with arithmetic formula

## Code Coverage

- Before: ~60%
- After: ~90%
- Removed `unused_function` to improve coverage

## Fix Summary

- Removed unused code and imports
- Optimized performance in `expensive_op`
- Used list comprehension in `slow_func`
- Verified improvements with tools
