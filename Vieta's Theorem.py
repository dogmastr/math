"""

    Author: @dogmastr
    Description: Converts roots of a monic polynomial to its coefficients and vice versa using Vieta's Theorem.

"""

import itertools

# Given roots r0, r1, ..., rn, we can reconstruct the polynomial using Vieta's Theorem.
def vieta(roots):

    n = len(roots)
    coefficients = [0] * (n+1)
    coefficients[0] = 1 # Leading coefficient of a monic.

    # For each coefficient a_k where k < n,
    # a_k = (-1)^k * sum of products of roots taken k at a time.
    for k in range(1, n+1):
        sum_products = 0
        for combo in itertools.combinations(roots, k):
            product = 1
            for r in combo:
                product *= r
            sum_products += product
        coefficients[k] = (-1)**k * sum_products

    return coefficients

# Given coefficients a_n, a_n-1, ..., a_0, we can compute the sum of the roots using the reverse Vieta's Theorem.
def vieta_reverse(coefficients):
    leading_coefficient = coefficients[0]
    
    # If our polynomial is non-monic, we divide each coefficient a_i by a_n.
    if leading_coefficient != 1:
        coefficients = [a_n / leading_coefficient for a_n in coefficients]
    
    # Note that in -coefficients[1] / leading_coefficient, our polynomial was already normalized to monic.
    return -coefficients[1]


"""
    
    Example Usage
    
"""

# Output: [1, -6, 11, -6], the polynomial reconstructed from its roots 1, 2, 3.
print(vieta([1, 2, 3]))

# Output: 6.0, the sum of the roots of x^3 - 6x^2 + 11x - 6.
print(vieta_reverse([1, -6, 11, -6]))