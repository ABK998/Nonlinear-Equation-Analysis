import matplotlib.pyplot as plt
import numpy as np
from sympy.solvers import solve
from sympy import N, re, im, diff, symbols, Abs
from sympy.parsing.sympy_parser import parse_expr

def constructed_exp(a, b, c, d, e, f, g, h, i, X):
    expr_str = f"({a}*X**4)/({b} + {c}*X) + ({d}*X**3)/({e} + {f}*X) + {g}*X**2 + {h}*X + {i}"
    return expr_str

fig, axis = plt.subplots(1, 2, figsize=(12, 5))

try:
    a = float(input("Enter the value for a: "))
    b = float(input("Enter the value for b: "))
    c = float(input("Enter the value for c: "))
    d = float(input("Enter the value for d: "))
    e = float(input("Enter the value for e: "))
    f = float(input("Enter the value for f: "))
    g = float(input("Enter the value for g: "))
    h = float(input("Enter the value for h: "))
    i = float(input("Enter the value for i: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

X = symbols('X')
expr_str = constructed_exp(a, b, c, d, e, f, g, h, i, X)
expr = parse_expr(expr_str)
print(f"Equation: {expr}")

try:
    res = solve(expr, X)
    print(f"Solutions: {res}")

    stability_results = []

    for i, r in enumerate(res):
        value = N(re(r), 6)
        print(f"Root {i+1}: X = {value}")

        derivative = diff(expr, X)
        stability = derivative.subs(X, r)
        stability_status = "Unstable" if re(stability) > 0 else "Stable"
        stability_results.append((value, stability_status))
        print(f"Stability at Root {i+1}: {stability_status} (Derivative: {stability})")

except Exception as e:
    print(f"An error occurred: {e}")

x = np.linspace(-10, 10, 10000)
y = [(a*n**4)/(b + c*n) + (d*n**3)/(e + f*n) + g*n**2 + h*n + i for n in x]

axis[0].plot(x, y, c="red")
axis[0].axvline(x=0, c="black", linewidth=0.5)
axis[0].axhline(y=0, c="black", linewidth=0.5)
axis[0].set_xlabel("X")
axis[0].set_ylabel("f(X)")
axis[0].set_title("Graph of f(X)")
axis[0].grid()

def func(a, b, c, d, e, f, g, h, i, n):
    return (a*n**4)/(b + c*n) + (d*n**3)/(e + f*n) + g*n**2 + h*n + i

size = 10000
a_samples = np.random.uniform(0.1, 1, size)
b_samples = np.random.uniform(0.1, 1, size)
c_samples = np.random.uniform(0.1, 1, size)
d_samples = np.random.uniform(0.1, 1, size)
e_samples = np.random.uniform(0.1, 1, size)
f_samples = np.random.uniform(0.1, 1, size)
g_samples = np.random.uniform(0.1, 1, size)
h_samples = np.random.uniform(0.1, 1, size)
i_samples = np.random.uniform(0.1, 1, size)
n_samples = np.random.uniform(0, 100, size)

outputs = func(a_samples, b_samples, c_samples, d_samples, e_samples, f_samples, g_samples, h_samples, i_samples, n_samples)
output_variance = np.var(outputs)

a_contribution = np.var(func(a_samples, b_samples.mean(), c_samples.mean(), d_samples.mean(), e_samples.mean(), f_samples.mean(), g_samples.mean(), h_samples.mean(), i_samples.mean(), n_samples)) / output_variance
b_contribution = np.var(func(a_samples.mean(), b_samples, c_samples.mean(), d_samples.mean(), e_samples.mean(), f_samples.mean(), g_samples.mean(), h_samples.mean(), i_samples.mean(), n_samples)) / output_variance
c_contribution = np.var(func(a_samples.mean(), b_samples.mean(), c_samples, d_samples.mean(), e_samples.mean(), f_samples.mean(), g_samples.mean(), h_samples.mean(), i_samples.mean(), n_samples)) / output_variance
d_contribution = np.var(func(a_samples.mean(), b_samples.mean(), c_samples.mean(), d_samples, e_samples.mean(), f_samples.mean(), g_samples.mean(), h_samples.mean(), i_samples.mean(), n_samples)) / output_variance

sensitivity_values = {"a": a_contribution, "b": b_contribution, "c": c_contribution, "d": d_contribution}

axis[1].bar(sensitivity_values.keys(), sensitivity_values.values(), 0.2, color="red")
axis[1].set_xlabel("Parameters")
axis[1].set_ylabel("Sensitivity")
axis[1].set_title("Sensitivity Analysis")

for root, status in stability_results:
    axis[0].plot(root, 0, marker='o', markersize=8, label=f'{status} At: X={root:.3f}', color='green' if status == "Stable" else 'blue')

fig.canvas.manager.set_window_title('Equation Analysis')
fig.text(0.5, 1, f"Parameters: a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}, i={i}", fontsize=16, fontweight=400, ha='center', va='top')
fig.subplots_adjust(wspace=1, left=0.06, right=0.97)
axis[0].legend(title='For real parts')
axis[0].grid()

plt.show()
