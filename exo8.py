import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Définition des points du quart de cercle
k = np.arange(4)
T = k * np.pi / 6  # Paramètre t_k
X = np.sin(T)
Y = np.cos(T)

# Spline directe sur (X, Y)   -> imposer X et en déduire Y
spline_direct = CubicSpline(X, Y)

# Spline paramétrique -> imposer T et en déduire X et Y
spline_x = CubicSpline(T, X)
spline_y = CubicSpline(T, Y)

# Évaluation des courbes
t_fine = np.linspace(0, np.pi/2, 100)
x_fine = np.sin(t_fine)
y_fine = np.cos(t_fine)

x_spline = np.linspace(0, 1, 100)  # Intervalle des X pour spline directe
y_spline = spline_direct(x_spline)

x_param = spline_x(t_fine)
y_param = spline_y(t_fine)

# Tracé des courbes
plt.figure(figsize=(8, 8))
plt.plot(x_fine, y_fine, 'k--', label="Quart de cercle réel")
plt.plot(x_spline, y_spline, 'r', label="Interpolation directe (X, Y)")
plt.plot(x_param, y_param, 'b', label="Interpolation paramétrique")
plt.scatter(X, Y, color='black', label="Points donnés")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparaison des interpolations")
plt.axis("equal")
plt.grid()

# Cercle complet avec la représentation paramétrique
t_circle = np.linspace(0, 2*np.pi, 100)
x_circle = np.cos(t_circle)
y_circle = np.sin(t_circle)

plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, 'g', label="Cercle complet")
plt.scatter(X, Y, color='black', label="Points quart de cercle")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cercle complet par représentation paramétrique")
plt.axis("equal")
plt.grid()

plt.show()
 
