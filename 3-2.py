import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Definir los puntos
x_points = np.array([0, 1, 2, 3])
y_points = np.array([1, 2, 33, 244])

# Construir el trazador cúbico
f_cubico = interp1d(x_points, y_points, kind='cubic', fill_value="extrapolate")

# Estimar el valor correspondiente a x = 2.7 usando el trazador cúbico
x_est = 2.7
y_est = f_cubico(x_est)

# Generar valores para graficar el trazador cúbico
x_values = np.linspace(0, 3, 500)  # Asegurarse de que x_values esté dentro del intervalo de interpolación
y_values = f_cubico(x_values)

# Graficar el trazador cúbico
plt.plot(x_values, y_values, label='Trazador Cúbico', color='green')
plt.scatter(x_points, y_points, color='red', zorder=5, label='Puntos Originales')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trazador Cúbico')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar el valor estimado
print(f"Para x = {x_est}, el valor estimado de y es {y_est:.2f}")
