import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, cumulative_trapezoid

# Definir el perfil h(x)
# Fondo seno
def h(x):
    return 1 + 0.5 * np.sin(x)
def dh(x):
    return 0.5 * np.cos(x)

# Parámetro alpha
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
ci1 = q0 = 1.147
ci2 = dq0 = 0.032
y0 = [q0, dq0]

x_span = [0* np.pi, 2 * np.pi]
x_eval = np.linspace(x_span[0], x_span[1], 500)

sol = solve_ivp(f, x_span, y0, t_eval=x_eval, method='Radau')

if sol.success:
    x = sol.t
    q_x = sol.y[0] # q(x)
    # Evitar divisiones por 0
    q_x[q_x < 1e-6] = 1e-6
    # Calcular la integral para obtener psi(x)
    integrand = alpha / (h(x) * q_x**2)
    psi_x = np.insert(cumulative_trapezoid(integrand, x), 0, 0) # Integral acumulativa
    # La instrucción insert añade un 0 al principio del array.
    # La función cumulative trapezoid integra entre cada dos nodos lo cual da un array
    # de tamaño 1 menos de lo que deberia ser

# Graficar los resultados
fig, ax = plt.subplots(2, 1, figsize=(8, 6))
ax[0].plot(x, q_x, label="q(x)", color="b")
ax[0].set_ylabel("q(x)")
ax[0].grid()
ax[1].plot(x, psi_x, label="psi(x) = ( / (h q²)) dx", color="r")
ax[1].set_xlabel("Espacio x")
ax[1].set_ylabel("psi(x)")
ax[1].grid()
plt.title("q y psi")
plt.show()