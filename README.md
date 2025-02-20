# Non-Linear Equation Solver, Sensitivity, Stability, and Variance Analysis

## Overview
This Python project solves a **non-linear equation** and analyzes the stability of its roots. Additionally, it performs **sensitivity analysis** to understand how different parameters affect the function.

## Features
- **Solves a non-linear equation** for given parameters.
- **Performs stability analysis** using the derivative of the function.
- **Plots the function f(X)** and highlights equilibrium points.
- **Conducts sensitivity analysis** to determine the impact of parameters on function behavior.

## Requirements
Make sure you have the following dependencies installed before running the script:

```bash
pip install numpy matplotlib sympy
```

## Usage
Run the Python script using:

```bash
python script.py
```

The program will prompt you to enter values for the parameters:
- **a, b, c, d, e, f, g, h, i**

After entering the values, it will:
1. Display the constructed equation.
2. Solve for equilibrium points (roots of f(X)).
3. Analyze the stability of the roots using the function's derivative.
4. Plot the function along with equilibrium points.
5. Perform sensitivity analysis and generate a bar graph.

## Equation
The script solves the following equation:

$$
f(X) = \frac{b + cX}{aX^4} + \frac{e + fX}{dX^3} + gX^2 + hX + i
$$

## Example
If the parameters are:

$$
a = 1.2, \quad b = 0.8, \quad c = 0.5, \quad d = 1.0, \quad e = 0.3, \quad f = 2.0, \quad g = 1.5, \quad h = -0.5, \quad i = 3.0
$$

Then the equation solved is:

$$
f(X) = \frac{0.8 + 0.5X}{1.2X^4} + \frac{0.3 + 2.0X}{1.0X^3} + 1.5X^2 - 0.5X + 3.0
$$

## Output
The script generates:
- A **graph of f(X)** with equilibrium points marked.
- A **bar chart for sensitivity analysis**.
- Printed **roots and their stability** in the console.

![Equation Analysis](Analysis_Graph.png)

## Contribution
Feel free to contribute by opening an issue or submitting a pull request!

## License
This project is open-source and licensed under the MIT License.
