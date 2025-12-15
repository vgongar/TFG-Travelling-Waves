import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, cumulative_trapezoid
from matplotlib.animation import FuncAnimation
from math import sqrt
# Definir el perfil h(x)
# Fondo seno
def h(x):
    return 1 + 0.5 * np.sin(x)
def dh(x):
    return 0.5 * np.cos(x)
# Condiciones iniciales
ci1 = q0 = 1.147
ci2 = dq0 = 0.032
y0 = [q0, dq0]

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

x_span = [0* np.pi, 2 * np.pi]
x_eval = np.linspace(x_span[0], x_span[1], 500)

# Resolver la EDO
sol = solve_ivp(f, x_span, y0, t_eval=x_eval, method='Radau')

if sol.success:
    x = sol.t
    q_x = sol.y[0] # q(x)
    # Calcular la integral para obtener psi(x)
    integrand = alpha / (h(x) * q_x**2)
    psi_x = np.insert(cumulative_trapezoid(integrand, x), 0, 0) # Integral acumulativa
    # La instrucción insert añade un 0 al principio del array.
    # La función cumulative trapezoid integra entre cada dos nodos lo cual da un array
    # de tamaño 1 menos de lo que deberia ser

# VISUALIZACIÓN DE LA ANIMACIÓN
## Parámetros
T = 10 # Duración total en segundos
FPS = 30 # Cuadros por segundo
num_frames = int(FPS * T) # Total de cuadros
interval = 1000 / FPS # Intervalo en milisegundos (33.33 ms)

fig, ax = plt.subplots()
line_q, = ax.plot([], [],'b-', label='q(x)')
line_h, = ax.plot([], [],'r-', label='h(x)')
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(-5,5)

def init():
    line_q.set_data([], [])
    line_h.set_data([], [])
    return line_q, line_h

def update(frame):
    t = frame / FPS
    # Actualizar las lineas
    y_vals = q_x * np.cos(w * t - psi_x)
    y_vals_h = -h(x)
    line_q.set_data(x, y_vals)
    line_h.set_data(x, y_vals_h)
    return line_q, line_h
    
# Crear la animación
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init,
blit=True, interval=interval)
#ani.save("name.gif", writer="pillow", fps=30)
# ^ Quitar la almohadilla inicial para guardar la animación.
plt.show()