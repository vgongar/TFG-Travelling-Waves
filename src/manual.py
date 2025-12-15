import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from math import sqrt

# Definir el perfil h(x)
def h(x):
    return 1 + 0.5 * np.sin(x)
def dh(x):
    return 0.5 * np.cos(x)

# Parámetros
alpha = 0.25
w = 0.21 # <sqrt((1-|c|)/pi)=0.39...

# Definir la ecuación diferencial
def f(x, y):
    q = y[0] # q(x)
    dq = y[1] # q'(x)
    return_1 = dq
    return_2 = alpha**2 / (h(x)**2 * q**3) - w**2 / h(x) * q - (dh(x) / h(x)) * dq
    return [return_1, return_2]

# Condiciones iniciales
ci1 = q0 = sqrt(alpha/w)
ci2 = dq0 = 0

# CÁLCULO DE LA ÓRBITA

y0 = [q0, dq0]
poincare = [y0]
for k in range(100):
    x_span = [2*k* np.pi, 2 * (k+1) * np.pi]
    x_eval = np.linspace(x_span[0], x_span[1], 500)
    sol = solve_ivp(f, x_span, y0, t_eval=x_eval, method='Radau')
    if sol.success:
        x = sol.t
        q_x = sol.y[0] # q(x)
        # Tomamos como condición inicial el último punto para la siguiente iteración
        q0 = q_x[-1]
        dq0 = sol.y[1][-1]
        y0 = [q0, dq0]
        poincare.append(y0)
        # Evitar divisiones por 0
        q_x[q_x < 1e-6] = 1e-6
    else:
        print("Error: La integración falló.")

# Separar los valores en listas de x e y
x_values, y_values = zip(*poincare)

# VISUALIZACIÓN

# Crear scatter plot con colores basados en el índice
indices = np.arange(len(poincare)) # Índices para los colores
plt.scatter(x_values, y_values, c=indices, cmap='viridis', marker='o')
plt.colorbar(label="Índice del punto")
plt.xlabel("q")
plt.ylabel("q'")
plt.suptitle(f"q0 = {ci1}, q1 = {ci2}")
plt.title("Región obtenida")

# Mostrar la gráfica
plt.show()