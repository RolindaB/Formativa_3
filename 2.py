import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Definir la función
def f(x):
    return np.sin(2 * np.pi * x)

# Nodos en el intervalo [0, 1]
x_nodes = np.array([0, 0.33, 0.67, 1.0])
y_nodes = f(x_nodes)

# Ajustar un polinomio cuadrático a los nodos
coefficients = np.polyfit(x_nodes, y_nodes, 2)
polynomial = Polynomial(coefficients[::-1])  # Coefficients are in descending order

# Generar puntos para graficar
x_values = np.linspace(0, 1, 500)
y_values = f(x_values)
y_approx = polynomial(x_values)

# Graficar la función y la aproximación
plt.plot(x_values, y_values, label='f(x) = sin(2πx)', color='blue')
plt.plot(x_values, y_approx, label='Aproximación Cuadrática', color='red', linestyle='--')
plt.scatter(x_nodes, y_nodes, color='black', zorder=5, label='Nodos')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Aproximación Cuadrática de sin(2πx)')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir los coeficientes del polinomio cuadrático
print(f'Coeficientes del polinomio cuadrático: {coefficients}')
