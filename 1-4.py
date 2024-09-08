import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos
x = np.array([3.0, 4.5, 7.0, 9.0])
y = np.array([2.5, 1.0, 2.5, 0.5])

# Construcción del trazador cuadrático
f_cuadratico = interp1d(x, y, kind='quadratic')

# Estimar el valor para x = 5
x_est = 5.0
y_est = f_cuadratico(x_est)

print(f"Para x = {x_est}, el valor estimado de y es {y_est:.2f}")

# Graficar los puntos y el trazador cuadrático
x_new = np.linspace(3.0, 9.0, 100)
y_new = f_cuadratico(x_new)

plt.plot(x, y, 'o', label='Datos Originales')
plt.plot(x_new, y_new, '-', label='Trazador Cuadrático')
plt.scatter(x_est, y_est, color='red', label=f'Estimación en x = {x_est}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trazador Cuadrático por Tramos')
plt.legend()
plt.grid(True)
plt.show()

