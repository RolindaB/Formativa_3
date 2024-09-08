import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos
x = np.array([3.0, 4.5, 7.0, 9.0])
y = np.array([2.5, 1.0, 2.5, 0.5])

# Construir el trazador cúbico
f_cubico = interp1d(x, y, kind='cubic')

# Estimar el valor correspondiente a x = 5 usando el trazador cúbico
x_est = 5.0
y_est = f_cubico(x_est)

# Generar más puntos para graficar el trazador cúbico
x_new = np.linspace(3.0, 9.0, 100)
y_new = f_cubico(x_new)

# Graficar el trazador cúbico
plt.plot(x, y, 'o', label='Datos Originales')
plt.plot(x_new, y_new, '-', label='Trazador Cúbico', color='green')

# Graficar el punto estimado
plt.scatter(x_est, y_est, color='red', label=f'Estimación en x = {x_est}')

# Etiquetas y leyenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trazador Cúbico con Estimación en x = 5')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar el valor estimado
print(f"Para x = {x_est}, el valor estimado de y es {y_est:.2f}")
