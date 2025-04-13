# Static and Dynamic Code Analysis Report

## Static Analysis

**flake8**:
- Unused imports: `math`, `random`
- Unused function: `unused_function`

**pylint**:
- Function `slow_func` could be simplified
- Unused code found in `unused_function`

## Line Profiling

### Bottleneck:
- `expensive_op(n)` was the slowest function

### Fix:
- Rewrote using arithmetic formula:
  `n * (999 * 1000) // 2`
- Performance improved drastically

## Code Coverage

- Initial coverage: 60%
- Final coverage: 100% (after removing unused function and fully testing logic)

## Fix Summary

- Removed unused imports and dead code
- Rewrote slow loop with math formula
- Simplified function with list comprehension
- Improved test coverage and efficiency

