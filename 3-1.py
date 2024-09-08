import numpy as np
import matplotlib.pyplot as plt

# Definir los puntos
x_points = np.array([0, 1, 2, 3])
y_points = np.array([1, 2, 33, 244])

# Calcular los coeficientes del polinomio interpolante de Lagrange
coefficients = np.polyfit(x_points, y_points, 3)
polynomial = np.poly1d(coefficients)

# Calcular el valor del polinomio en x = 2.7
x_est = 2.7
y_est = polynomial(x_est)

# Generar valores para graficar el polinomio
x_values = np.linspace(-0.5, 3.5, 500)
y_values = polynomial(x_values)

# Graficar el polinomio interpolante
plt.plot(x_values, y_values, label='Polinomio Interpolante de Lagrange', color='green')
plt.scatter(x_points, y_points, color='red', zorder=5, label='Puntos Originales')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polinomio Interpolante de Lagrange')
plt.legend()
plt.grid(True)
plt.show()

# Imprimir el polinomio
print(f"Coeficientes del polinomio: {coefficients}")
print(f"Polinomio Interpolante: {polynomial}")

# Mostrar el valor estimado
print(f"Para x = {x_est}, el valor estimado de y es {y_est:.2f}")
