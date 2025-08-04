# Character Replacement Utility

This project provides a simple Python utility to replace specific characters in names with numbers, inspired by "leet speak". It also includes a Jupyter notebook for experimenting with character replacement and other string manipulation techniques.

## Files

- [`charReplace.py`](charReplace.py): Contains the main `charReplace` function that replaces characters in two names and prints the results.
- [`armin.ipynb`](armin.ipynb): Jupyter notebook with code cells for character counting and various character replacement methods.
- `README.md`: Project documentation.

## Usage

### Running the Script

To run the character replacement script:

```sh
python charReplace.py
```

This will output:

```
4rm1n 54r4
```

### Function Details

The [`charReplace`](charReplace.py) function replaces:
- `i` with `1`
- `a` with `4`
- `s` with `5`

Example:

```python
charReplace("armin", "sara")
# Output: 4rm1n 54r4
```

### Jupyter Notebook

Open [`armin.ipynb`](armin.ipynb) in JupyterLab or VS Code to explore:
- Counting the number of characters in a name
- Alternative methods for character replacement

## Requirements

- Python 3.6+
- (Optional) Jupyter Notebook for `.ipynb` file

## License

MIT License