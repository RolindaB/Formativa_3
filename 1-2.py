import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([3.0, 4.5, 7.0, 9.0])
y = np.array([2.5, 1.0, 2.5, 0.5])

# Graficar trazador lineal
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Trazador Lineal')

# Punto entre el que vamos a interpolar
x1, y1 = 4.5, 1.0
x2, y2 = 7.0, 2.5

# El valor de x que queremos estimar
x_est = 5.0

# Fórmula de interpolación lineal
y_est = y1 + (y2 - y1) / (x2 - x1) * (x_est - x1)

# Graficar el punto estimado para x = 5 en la gráfica del trazador lineal
plt.scatter(x_est, y_est, color='red', label=f'Estimación en x = {x_est}')

# Etiquetas y leyenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trazador Lineal con Estimación en x = 5')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar valor estimado
print(f"Para x = {x_est}, el valor estimado de y es {y_est:.2f}")

