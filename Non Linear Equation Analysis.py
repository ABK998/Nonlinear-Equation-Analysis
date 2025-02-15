"""
Solving a non-linear equation and Determining its Stability,Sensitivity and Variance Analysis.

"""

# Importing required libraries
import matplotlib.pyplot as plt
import numpy as np
from sympy.solvers import solve
from sympy import N, re, im, diff, symbols, Abs
from sympy.parsing.sympy_parser import parse_expr

# Function to construct the equation as a string
def constructed_exp(kappa, m, rho, sigma, C, Phi):
    expr_str = f"({kappa}**2)/(2*({m}**2 + {rho}*{kappa}))*{Phi}**3 + (3*{sigma}*{kappa})/(2*({m}**2 + {rho}*{kappa}))*{Phi}**2 + ({sigma}**2)/(2*({m}**2 + {rho}*{kappa}))*{Phi} + ({C}*{kappa})/(2*({m}**2 + {rho}*{kappa}))"
    return expr_str

# Setting up the plot
fig, axis = plt.subplots(1, 2, figsize=(12, 5))

# Taking user input for parameters
try:
    kappa = float(input("Enter the value for κ (kappa): "))
    m = float(input("Enter the value for m: "))
    rho = float(input("Enter the value for ρ (rho): "))
    sigma = float(input("Enter the value for σ (sigma): "))
    C = float(input("Enter the value for C: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

# Defining symbol for Φ
Phi = symbols('Phi')

# Constructing and parsing the mathematical expression
expr_str = constructed_exp(kappa, m, rho, sigma, C, Phi)
expr = parse_expr(expr_str)

# Formatting the equation for display
formatted_expr = str(expr).replace("Phi", "Φ")
print(f"Equation: {formatted_expr}")

# Solving the equation for roots
try:
    res = solve(expr, Phi)
    print(f"Solutions: {res}")

    stability_results = []
    stability_results_abs = []

    for i, r in enumerate(res):
        value = N(re(r), 6)
        print(f"Root {i+1}: Φ = {value}")

        # Compute derivative and evaluate stability
        derivative = diff(expr, Phi)
        stability = derivative.subs(Phi, r)
        stability_status_re = "Unstable" if re(stability) > 0 else "Stable"
        stability_results.append((value, stability_status_re))
        print(f"Stability at Root {i+1}: {stability_status_re} (Derivative: {stability})")

        # Alternative stability check using absolute value
        absolute_res = "Stable" if Abs(N(Abs(stability), 6)) <= 1 else "Unstable"
        stability_results_abs.append((r, absolute_res))

    # Display stability analysis
    print("\nStability Analysis (Real part of Eigenvalues):")
    for root, status in stability_results:
        print(f"Root: Φ = {root}, Status: {status}")

    print("\nStability Analysis (Absolute value of Eigenvalues):")
    for root, status in stability_results_abs:
        print(f"Root: Φ = {root}, Status: {status}")

except Exception as e:
    print(f"An error occurred: {e}")

# Plotting the function f(Φ)
x = np.linspace(-10, 10, 10000)
y = [(kappa**2)/(2*(m**2 + rho*kappa))*n**3 + (3*sigma*kappa)/(2*(m**2 + rho*kappa))*n**2 +
     (sigma**2)/(2*(m**2 + rho*kappa))*n + (C*kappa)/(2*(m**2 + rho*kappa)) for n in x]

axis[0].plot(x, y, c="red")
axis[0].axvline(x=0, c="black", linewidth=0.5)
axis[0].axhline(y=0, c="black", linewidth=0.5)
axis[0].set_xlabel("Φ")
axis[0].set_ylabel("f(Φ)")
axis[0].set_title("Graph of f(Φ)")
axis[0].grid()

# Sensitivity Analysis Function
def func(kappa, m, rho, sigma, C, n):
    return (kappa**2)/(2*(m**2 + rho*kappa))*n**3 + (3*sigma*kappa)/(2*(m**2 + rho*kappa))*n**2 + \
           (sigma**2)/(2*(m**2 + rho*kappa))*n + (C*kappa)/(2*(m**2 + rho*kappa))

# Generating random samples for sensitivity analysis
size = 10000
kappa_samples = np.random.uniform(0.1, 1, size)
m_samples = np.random.uniform(0.1, 1, size)
rho_samples = np.random.uniform(0.1, 1, size)
C_samples = np.random.uniform(0.1, 1, size)
sigma_samples = np.random.uniform(0.1, 1, size)
n_samples = np.random.uniform(0, 100, size)

outputs = func(kappa_samples, m_samples, rho_samples, sigma_samples, C_samples, n_samples)
output_variance = np.var(outputs)

# Sensitivity contribution calculations
kappa_contribution = np.var(func(kappa_samples, m_samples.mean(), rho_samples.mean(), sigma_samples.mean(), C_samples.mean(), n_samples)) / output_variance
m_contribution = np.var(func(kappa_samples.mean(), m_samples, rho_samples.mean(), sigma_samples.mean(), C_samples.mean(), n_samples)) / output_variance
rho_contribution = np.var(func(kappa_samples.mean(), m_samples.mean(), rho_samples, sigma_samples.mean(), C_samples.mean(), n_samples)) / output_variance
C_contribution = np.var(func(kappa_samples.mean(), m_samples.mean(), rho_samples.mean(), sigma_samples.mean(), C_samples, n_samples)) / output_variance
sigma_contribution = np.var(func(kappa_samples.mean(), m_samples.mean(), rho_samples.mean(), sigma_samples, C_samples.mean(), n_samples)) / output_variance

# Plotting Sensitivity Analysis
sensitivity_values = {"κ": kappa_contribution, "m": m_contribution, "ρ": rho_contribution, "C": C_contribution, "σ": sigma_contribution}

axis[1].bar(sensitivity_values.keys(), sensitivity_values.values(), 0.2, color="red")
axis[1].set_xlabel("Parameters")
axis[1].set_ylabel("Sensitivity")
axis[1].set_title("Sensitivity Analysis")

# Marking roots on the plot
for root, status in stability_results:
    axis[0].plot(root, 0, marker='o', markersize=8, label=f'{status} At: Φ={root:.3f}', color='green' if status == "Stable" else 'blue')

# Formatting the figure
fig.canvas.manager.set_window_title('Equation Analysis')
fig.text(0.5, 0.95, f"Equation f(Φ) = {formatted_expr}", fontsize=12, fontweight=400, ha='center', va='top')
fig.text(0.5, 0.88, "Roots (Equilibrium Points)", fontsize=14, fontweight=600, ha='center', va='top')
for i, root in enumerate(res):
    fig.text(0.5, 0.82 - i*0.06, f"Φ={N(root, 6)}", fontsize=14, fontweight=400, ha='center', va='top')

fig.text(0.5, 1, f"Parameters: κ={kappa}, m={m}, ρ={rho}, σ={sigma}, C={C}", fontsize=16, fontweight=400, ha='center', va='top')
fig.subplots_adjust(wspace=1, left=0.06, right=0.97)
axis[0].legend(title='For real parts')
axis[0].grid()

# Show the plots
plt.show()
