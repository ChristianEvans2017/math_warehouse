### test_custom_functions.py ###

import math
import cmath

def safe_sqrt(x):
    if isinstance(x, complex):
        return cmath.sqrt(x)
    elif x < 0:
        return cmath.sqrt(x)
    else:
        return math.sqrt(x)

def quadratic_formula(a, b, c):
    return ((-b-safe_sqrt(b**2-4*a*c))/(2*a),(-b+safe_sqrt(b**2-4*a*c))/(2*a))