"""

    Author: @dogmastr
    Description: Implementation of a three-point central difference formula to approximate the first derivative at x0.

"""

import math
import sys

def f(x):
    return math.sin(x)

def f_second_derivative(x):
    return math.cos(x)

x0 = math.pi / 4

# A formula for the step size h that balances the rounding error against the secant error for optimum accuracy is:
# h = 2 * sqrt(epsilon * |f(x) / f''(x)|)
machine_epsilon = sys.float_info.epsilon # This is the smallest positive floating-point number such that 1.0 + epsilon != 1.0
h = 2 * math.sqrt(machine_epsilon * abs(f(x0) / f_second_derivative(x0)))

# The three-point central difference formula to approximate f'(x) with step size h.
def three_point_central_difference(f, x0, h):
    return (f(x0 + h) - f(x0 - h)) / (2 * h)

"""

    Example Usage

"""

approximated_derivative = three_point_central_difference(f, x0, h)
true_derivative = math.cos(x0)

print(f"Approximated derivative: {approximated_derivative}")
print(f"True derivative: {true_derivative}")
print(f"Error: {abs(approximated_derivative - true_derivative)}")
