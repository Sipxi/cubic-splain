# Cubic Spline Interpolation in Python

## Overview
This Python script implements cubic spline interpolation using the `sympy` library. It takes a set of coordinates as input, constructs the interpolation polynomial, and solves for `y`.


## Requirements
- Python 3.x
- `sympy` library

## Installation
Ensure you have Python installed, then install `sympy` if not already available:
```bash
pip install sympy
```

## Usage
Run the script in a terminal:
```bash
python cubic_spline.py
```
Follow the prompts to enter the number of coordinates and their values. The script will output the interpolated equation.

## Example
```
Enter number of coordinates: 3
x0: 1
y0: 2
x1: 3
y1: 4
x2: 5
y2: 6
```
Output:
```
Solution is: y = <Cubic Spline Interpolated Function>
```

## Notes
- The script uses `os.system('cls')` to clear the screen (for Windows). Modify it to `os.system('clear')` for Linux/macOS.
- Cubic spline interpolation provides a smoother approximation compared to polynomial interpolation.

## License
This project is open-source and available for modification.

