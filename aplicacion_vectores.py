"""
Aplicación práctica de vectores: navegación de un dron con viento.
El programa calcula la velocidad que debe generar el dron para que,
considerando el viento, su velocidad resultante apunte hacia el destino.
"""

import numpy as np
import matplotlib.pyplot as plt

# Punto inicial y destino en metros
A = np.array([0.0, 0.0])
B = np.array([120.0, 80.0])

# Velocidad deseada respecto al suelo y viento, en m/s
rapidez_deseada = 50.0
viento = np.array([15.0, -10.0])

# Vector de dirección hacia el destino
trayecto = B - A
direccion_unitaria = trayecto / np.linalg.norm(trayecto)

# Velocidad resultante deseada respecto al suelo
velocidad_suelo = rapidez_deseada * direccion_unitaria

# Velocidad que debe producir el dron respecto al aire
velocidad_dron = velocidad_suelo - viento
modulo_velocidad_dron = np.linalg.norm(velocidad_dron)

print("Dirección unitaria hacia el destino:", direccion_unitaria)
print("Velocidad deseada respecto al suelo:", velocidad_suelo)
print("Vector viento:", viento)
print("Velocidad requerida del dron:", velocidad_dron)
print("Módulo de la velocidad requerida del dron:", modulo_velocidad_dron)

# Gráfica vectorial
plt.figure(figsize=(7, 6))
plt.quiver(A[0], A[1], trayecto[0], trayecto[1], angles="xy", scale_units="xy", scale=1, label="Trayecto A→B")
plt.quiver(0, 0, velocidad_suelo[0], velocidad_suelo[1], angles="xy", scale_units="xy", scale=1, label="Velocidad resultante")
plt.quiver(0, 0, viento[0], viento[1], angles="xy", scale_units="xy", scale=1, label="Viento")
plt.quiver(0, 0, velocidad_dron[0], velocidad_dron[1], angles="xy", scale_units="xy", scale=1, label="Velocidad del dron")

plt.scatter([A[0], B[0]], [A[1], B[1]])
plt.text(A[0] + 2, A[1] + 2, "A")
plt.text(B[0] + 2, B[1] + 2, "B")
plt.xlim(-10, 140)
plt.ylim(-30, 100)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Aplicación de vectores en navegación de un dron")
plt.grid(True)
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")
plt.tight_layout()
plt.savefig("../figs/vector_aplicacion_dron.png", dpi=300)
plt.show()
