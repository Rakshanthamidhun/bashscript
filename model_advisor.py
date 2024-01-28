import numpy as np
from scipy.optimize import curve_fit

def linear_function(x, m):
    return m * x

def circular_function(x, a, b):
    return np.sqrt(b**2 - (x - a)**2)

def hyperbolic_function(x, a, b):
    return b / (x - a)

def parabolic_function(x, a, b, c):
    return a * x**2 + b * x + c

def elliptical_function(x, a, b):
    return b * np.sqrt(1 - (x/a)**2)

def fit_curve(func, x, y):
    popt, pcov = curve_fit(func, x, y)
    return popt

def check_function_type(x, y):
    # Fit a linear curve
    linear_params = fit_curve(linear_function, x, y)
    
    # Fit a circular curve
    circular_params = fit_curve(circular_function, x, y)
    
    # Fit a hyperbolic curve
    hyperbolic_params = fit_curve(hyperbolic_function, x, y)
    
    # Fit a parabolic curve
    parabolic_params = fit_curve(parabolic_function, x, y)
    
    # Fit an elliptical curve
    elliptical_params = fit_curve(elliptical_function, x, y)
    
    return {
        'linear': linear_params,
        'circular': circular_params,
        'hyperbolic': hyperbolic_params,
        'parabolic': parabolic_params,
        'elliptical': elliptical_params
    }

# Provided data
time_steps = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
outputs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])

# Check function type
function_types = check_function_type(time_steps, outputs)

# Output the results
for function, params in function_types.items():
    print(f"{function.capitalize()} function parameters: {params}")
