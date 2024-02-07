import numpy as np 

def Taylor_interpolation(f, a, x):
    # Calculate the first derivative of f(x)
    f_prime = (f(a + 0.00001) - f(a - 0.00001)) / (2 * 0.00001)
    
    # Calculate the first-order Taylor approximation
    approximation = f(a) + f_prime * (x - a)
    
    return approximation


#Testing function

# Define the function f(x) = sin(x)
def f(x):
    return np.sin(x)

# Set the point of expansion a = pi/4
a = np.pi/4

# Set the value of x = pi/2
x = np.pi/2

# Calculate the interpolated value using Taylor_interpolation
interpolated_value = Taylor_interpolation(f, a, x)

print(f"El valor interpolado de f es -> {x:.4f} \nUsando la aproximación de Taylor de primer orden es -> {interpolated_value:.4f}")
