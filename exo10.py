import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# Données
annees = np.array([1975, 1980, 1985, 1990])
duree_vie = np.array([70.2, 70.2, 70.3, 71.2])

# Interpolation polynomiale de Lagrange
poly = lagrange(annees, duree_vie)

# Spline cubique
spline = CubicSpline(annees, duree_vie)
spline_natural = CubicSpline(annees, duree_vie, bc_type='natural')

# Extrapolation pour 1970 et 1995
extrapolation_1970_poly = poly(1970)
extrapolation_1995_poly = poly(1995)
extrapolation_1970_spline = spline(1970)
extrapolation_1995_spline = spline(1995)

# Affichage des résultats
print("Extrapolation en 1970:")
print(f" - Par interpolation polynomiale: {extrapolation_1970_poly:.2f} ans")
print(f" - Par spline cubique: {extrapolation_1970_spline:.2f} ans")
#avec la spline naturelle
extrapolation_1970_spline_natural = spline_natural(1970)
print(f" - Par spline cubique naturelle: {extrapolation_1970_spline_natural:.2f} ans")
print("Durée de vie observée en 1970: 69.6 ans")

erreur_poly_1970 = abs(extrapolation_1970_poly - 69.6)
erreur_spline_1970 = abs(extrapolation_1970_spline - 69.6)

print(f"Erreur de l'interpolation polynomiale: {erreur_poly_1970:.2f} ans")
print(f"Erreur de la spline cubique: {erreur_spline_1970:.2f} ans")
#avec la spline naturelle
erreur_spline_natural_1970 = abs(extrapolation_1970_spline_natural - 69.6)
print(f"Erreur de la spline cubique naturelle: {erreur_spline_natural_1970:.2f} ans")


print("\nExtrapolation en 1995:")
print(f" - Par interpolation polynomiale: {extrapolation_1995_poly:.2f} ans")
print(f" - Par spline cubique: {extrapolation_1995_spline:.2f} ans")

#avec la spline naturelle
extrapolation_1995_spline_natural = spline_natural(1995)
print(f" - Par spline cubique naturelle: {extrapolation_1995_spline_natural:.2f} ans")

# Estimation de la précision pour 1995
precision_1995_poly = erreur_poly_1970
precision_1995_spline = erreur_spline_1970
print(f"\nEstimation de l'erreur pour 1995 sur base de 1970:")
print(f" - Interpolation polynomiale: ±{precision_1995_poly:.2f} ans")
print(f" - Spline cubique: ±{precision_1995_spline:.2f} ans")
#avec la spline naturelle
precision_1995_spline_natural = erreur_spline_natural_1970
print(f" - Spline cubique naturelle: ±{precision_1995_spline_natural:.2f} ans")

# Tracé des interpolations
x_vals = np.linspace(1965, 2000, 200)
y_vals_poly = poly(x_vals)
y_vals_spline = spline(x_vals)
y_vals_spline_natural = spline_natural(x_vals)

plt.figure(figsize=(8,6))
plt.scatter(annees, duree_vie, color='red', label='Données')
plt.plot(x_vals, y_vals_poly, '--', label='Interpolation polynomiale')
plt.plot(x_vals, y_vals_spline, '-', label='Spline cubique')
plt.plot(x_vals, y_vals_spline_natural, '-', label='Spline cubique naturelle')
plt.axvline(1970, color='gray', linestyle=':', label='1970')
plt.axvline(1995, color='gray', linestyle=':', label='1995')
plt.xlabel('Année')
plt.ylabel('Durée de vie moyenne')
plt.legend()
plt.title("Interpolation et extrapolation de la durée de vie moyenne")
plt.show()
 
