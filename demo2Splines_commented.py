#
# Splines cubiques
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

from numpy import *

n = 21
L = 1
X = linspace(-L,L,n)      # ; print(X)  # Pour debugger step by step      # créer n-1 intervalles entre -L et L (intervalles entre lesquels on veut créer les splines) 
U = sin(2*pi*X)           # ; print(U)  # Pour debugger step by step      # évaluer la fonction sin(2*pi*x) en chaque point de X -> ce sont les points que l'on veut interpoler --- Attention : U est bien un vecteur numpy

x = linspace(-L,L,10*n) #création de 10*n points entre -L et L pour tracer les splines (Attention : ce vecteur ne détermine pas les points à interpoler mais uniquement les poitns qu'one tracera sur les graphiques)

#
# -1- Accéder aux données d'un tableau
#     Assez proche de la syntaxe de MATLAB
#     Attention : on numérote à partir de zero en Python
#       X[0:21:2] Python = MATLAB X(1:2:20)
#

print(X)
print(X[:])
print(X[0:10])
print(X[0:21:2]) #afficher les éléments de 0 à 20 avec un pas de 2

#
# -2- Une copie et une vue d'un tableau
#     Attention : ceci est différent de MATLAB !
#     =====> beaucoup de bugs vicieux possibles....
#     Y = une vue du même espace mémoire
#     Z = une vraie copie du mémoire
#

Y = X[0:21:2] 
Y[0] = 69;    print('X[0] = %3d - Y[0] = %3d' % (X[0],Y[0]))  #essayez de déduire quelles seront les valeurs affichées avant de lancer le programme
X[0] = 456;   print('X[0] = %3d - Y[0] = %3d' % (X[0],Y[0]))
X[0] = -1;    print('X[0] = %3d - Y[0] = %3d' % (X[0],Y[0]))
Z = copy(X)
Z[0] = 69;    print('X[0] = %3d - Y[0] = %3d - Z[0] = %3d' % (X[0],Y[0],Z[0]))  #essayez de déduire quelles seront les valeurs affichées avant de lancer le programme
X[0] = 456;   print('X[0] = %3d - Y[0] = %3d - Z[0] = %3d' % (X[0],Y[0],Z[0]))
X[0] = -1;    print('X[0] = %3d - Y[0] = %3d - Z[0] = %3d' % (X[0],Y[0],Z[0]))

#
# -3- Calcul des splines cubiques
#

from scipy.interpolate import CubicSpline as spline

uSpline1 = spline(X[0:10],U[0:10])(x) #calcul de la spline cubique sur les 10 premiers points -> l'argument x est le vecteur des points où on veut évaluer la spline pour la tracer par la suite MAIS pas les intervalles auquels la spline est associée
uSpline2 = spline(X[0:21:2],U[0:21:2])(x) #calcul de la spline cubique sur un point sur deux

#
# -4- Et le joli dessin :-)
#

import matplotlib 
from matplotlib import pyplot as plt

plt.plot(x,uSpline1,'-b',label='spline sur les 10 premiers point')
plt.plot(x,uSpline2,'-r',label='spline sur un point sur deux')
plt.plot(X[0:10],U[0:10],'.b',markersize=20,label='10 premiers points')
plt.plot(X[0:21:2],U[0:21:2],'.r',markersize=10,label='1 point sur 2')
plt.legend(loc='upper right')
plt.show()

