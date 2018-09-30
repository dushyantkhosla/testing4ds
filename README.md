# Testing for Data Scientists

## Why Testing

- Find bugs
- Check your assumptions by making them explicit
- Test outcomes, not the implementation

## When to test?

- Write tests as you develop the code
  (*or before, if you're using TDD*)
- When you find a bug, add a test.

## Types of Tests

- Unit
  - define input, output, expected behavior
  - run on internal (module) code only 
  - often automated, run before software merge/release cycles
  - code coverage measures lines exercised by unit tests
- Integration

## Docstrings, Syntax and Type Checking

- **Write clear docstrings**
  - What is the function's purpose
  - What objects and parameters does it take and return
- **Put examples in the docstring**
  Create an <u>example</u> at the interactive prompt and paste it in the docstring
  (People mostly skip reading the docstring and go straight to examples) 
  - The `doctest` module creates tests out of docstring examples
  - It finds the interactive prompt text and re-creates test results

```python
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
```

- **Detect common errors with `pyflakes`** 
  - Unused imports, undeclared variables etc. will be found

```bash
python3 -m pyflakes quadratic.py
```

- **Put type checking in the code with `mypy`** 
  - Add type hints each time you declare a new data structure/function
  - `mypy` is able to follow the chain of commands and ensure they assemble properly

```bash
mypy quadratic.py
```

## Test Modules

### `pytest`

- Create a folder called `/tests` in your repo to hold files with test functions
- Write test functions that begin with `def test_<func-to-test>():`
  - test functions examine the output of module functions
  - ensure that module functions do as they advertize using `assert` statements
  - Example

```python
from my_module import get_data

def test_get_data():
    df = get_data()
    assert all(df.columns == ['A', 'B', 'C', 'D'])
    assert isinstance(df.index, pd.DatetimeIndex)
```

- Run tests as

```bash
python3 -m pytest my_module
```

- It will discover test functions (named as per convention) and run them
  See [conventions for Python test discovery](http://doc.pytest.org/en/latest/goodpractices.html#test-discovery).

### `hypothesis`

Find failing test cases with `hypothesis`

- Implements *property-based testing* 
- The *property* is invariant (always True) against which `hypothesis` runs many tests
  - Generate random inputs according to some strategies
  - Run function with different combinations
  - Essentially, it tortures the function until it fails
- We use the `given`, `assume` and `strategies` features of hypothesis to set up test space
- Useful for finding edge cases
- Ideal for code that accepts *free-text* input 

### `engarde`

- Built with pandas, very lightweight
- Use for functions that accept and return Dataframes
- Just add decorators! (or use `DataFrame.pipe()`)

```python
@is_shape(10**5, 16)
@none_missing()
@unique_index
def transform_input(df):
    ...
    return result
```

## Writing tests in Data Science

- Univariate
  - feature values within expected thresholds
  - feature stats (mean, stddev) within expected ranges
  - feature values following an expected statistical distribution
  - categorical features have expected number of levels
- Bivariate
  - correlation metric for pairs of features are satisfied
- DataFrame level
  - DataFrame has expected shape
  - Index is of expected type and shape

## References

Talks

- [Trey Causey](http://slides.com/treycausey/pydata2015#/)
- [Kathrine Jarmul](https://blog.kjamistan.com/data-unit-testing-europython-tutorial/)
- [Hillel Wayne](https://www.youtube.com/watch?v=MYucYon2-lk)

Links

- [pytest](https://docs.pytest.org/en/latest/contents.html)
- [hypothesis](https://hypothesis.readthedocs.io/en/latest/)
  - [Hypothesis' Pandas strategies](https://hypothesis.readthedocs.io/en/latest/numpy.html#pandas)
- [engarde](https://github.com/tomaugspurger/engarde) 
  - for testing `pandas.DataFrame` objects 
- [tdda](https://tdda.readthedocs.io/en/tdda-1.0.04/) 
  - for test-driven data analysis takes data inputs (such as NumPy arrays) and builds a set of constraints around them
- [voluptuous](https://github.com/alecthomas/voluptuous) 
  - for schema definitions
- [faker](https://faker.readthedocs.io/en/master/) 
  - generates fake data for you
