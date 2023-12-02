import numpy as np
import matplotlib.pyplot as plt

# Definir los coeficientes de las ecuaciones en una matriz
A = np.array([[-2, 5, 9], [7, 1, 1], [-3, 7, -1]])

# Definir los términos independientes en un vector
B = np.array([1, 6, -26])

# Crear una malla de puntos en el espacio
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)

# Calcular los valores de Z en función de las ecuaciones
Z1 = (1 - A[0, 0] * X - A[0, 1] * Y) / A[0, 2]
Z2 = (6 - A[1, 0] * X - A[1, 1] * Y) / A[1, 2]
Z3 = (-26 - A[2, 0] * X - A[2, 1] * Y) / A[2, 2]

# Graficar las ecuaciones como rectas en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X[0], X[1], X[2], 'ro', label='Intersección')
ax.plot_surface(X, Y, Z1, alpha=0.5)
ax.plot_surface(X, Y, Z2, alpha=0.5)
ax.plot_surface(X, Y, Z3, alpha=0.5)


# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la gráfica
plt.show()
