import numpy as np 

def Taylor_interpolation(f:callable, a:float, x:float) -> float:
    """Does first degree interpolation of a function.

    Args:
        f (function): function to approximate
        a (float): point of expansion
        x (float): interpolation point

    Returns:
        (float): interpolation of f around a at x.
    """
    # Calculate the first derivative of f(x)
    f_prime = (f(a + 1e-5) - f(a - 1e-5)) / (2 * 1e-5)
    
    # Calculate the first-order Taylor approximation
    approximation = f(a) + f_prime * (x - a)
    
    return approximation


#Testing function

# Define the function f(x) = sin(x)
def f(x):
    return np.sin(x)

if __name__ == "__main__":
    # Set the point of expansion a = pi/4
    a = np.pi/4

    # Set the value of x = pi/2
    x = np.pi/2

    # Calculate the interpolated value using Taylor_interpolation
    interpolated_value = Taylor_interpolation(f, a, x)

    print(f"El valor interpolado de f es -> {a:.4f}",
          f"Usando la aproximación de Taylor de primer orden es -> {interpolated_value:.4f}",
          sep="\n")
