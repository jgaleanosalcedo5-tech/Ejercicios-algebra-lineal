
import numpy as np
import matplotlib.pyplot as plt

# Puntos de apoyo de la rampa
A = np.array([0, 0, 0])
B = np.array([4, 0, 1])
C = np.array([0, 3, 1.5])

# Vectores del plano
AB = B - A
AC = C - A

# Vector normal usando producto cruz
normal = np.cross(AB, AC)
print("Vector normal:", normal)

# Ecuacion simplificada: x + 2y - 4z = 0
# Despeje: z = (x + 2y) / 4

x = np.linspace(0, 4, 20)
y = np.linspace(0, 3, 20)
X, Y = np.meshgrid(x, y)
Z = (X + 2 * Y) / 4

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z, alpha=0.7)
ax.scatter([A[0], B[0], C[0]],
           [A[1], B[1], C[1]],
           [A[2], B[2], C[2]],
           s=50)

ax.set_title("Plano de una rampa")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.savefig("plano_rampa.png", dpi=300)
plt.show()
