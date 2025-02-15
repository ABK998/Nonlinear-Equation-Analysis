# Non-Linear Equation Solver and Stability Analysis

## Overview
This Python project solves a **non-linear equation** and analyzes the stability of its roots. Additionally, it performs **sensitivity analysis** to understand how different parameters affect the function.

## Features
- **Solves a non-linear equation** for given parameters.
- **Performs stability analysis** using the derivative of the function.
- **Plots the function f(\u03A6)** and highlights equilibrium points.
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
- **\u03BA (kappa)**
- **m**
- **\u03C1 (rho)**
- **\u03C3 (sigma)**
- **C**

After entering the values, it will:
1. Display the constructed equation.
2. Solve for equilibrium points (roots of f(\u03A6)).
3. Analyze the stability of the roots using the function's derivative.
4. Plot the function along with equilibrium points.
5. Perform sensitivity analysis and generate a bar graph.

## Output
The script generates:
- A **graph of f(\u03A6)** with equilibrium points marked.
- A **bar chart for sensitivity analysis**.
- Printed **roots and their stability** in the console.

![Equation Analysis](Analysis_Graph.png)

## Example Equation
If the parameters are:
```
\u03BA = 1.2, m = 0.8, \u03C1 = 0.5, \u03C3 = 0.3, C = 2.0
```
Then the equation solved is:

```math
(\u03BA^2)/(2*(m^2 + \u03C1*\u03BA))*\u03A6^3 + (3*\u03C3*\u03BA)/(2*(m^2 + \u03C1*\u03BA))*\u03A6^2 + (\u03C3^2)/(2*(m^2 + \u03C1*\u03BA))*\u03A6 + (C*\u03BA)/(2*(m^2 + \u03C1*\u03BA)) = 0
```

The script will solve for \u03A6 and determine stability.

## Sensitivity Analysis
Sensitivity analysis helps understand how **small changes in parameters affect the roots of the equation**. The bar chart generated visually represents which parameters have the most influence.

## Contribution
Feel free to contribute by opening an issue or submitting a pull request!

## License
This project is open-source and licensed under the MIT License.

