"""Pending 3d graph"""

from sympy import solve, Eq, symbols
import numpy as np
from matplotlib import pyplot as plt

# Define equations
x,y,z = symbols("x y z")
eq1 = Eq(5*x - 3*y + 2*z, 20)
eq2 = Eq(4*x + 6*y - 5*z, -2)
eq3 = Eq(8*x + y - z, 21)

# Solve it
sol = solve((eq1, eq2, eq3), (x, y, z))

# Print result
print(eq1, eq2, eq3, sol, sep="\n")

# Graph result
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Axis setup for the graph
X = np.linspace(-5,5,10)
Y = np.linspace(-5,5,10)
X, Y = np.meshgrid(X, Y)

# Getting the Z values per equation
Z1 = (5 * X - 3 * Y - 20) / - 2
Z2 = (4 * X + 6 * Y + 2) / 5
Z3 = (8 * X + Y - 21) / 1

# Plot the planes
ax.plot_wireframe(X,Y, Z1, color="green")
ax.plot_wireframe(X,Y,Z2, color="red")
ax.plot_wireframe(X,Y,Z3, color="blue")

# Plot the point
ax.scatter(sol[x], sol[y], sol[z], color="orange")

plt.show()