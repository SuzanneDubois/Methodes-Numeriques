from numpy import *
from matplotlib import pyplot as plt

#début et fin de l'intervalle et conditions initiales
Xstart = 0; Xend = 4; Ustart = 1

#vecteur des valeurs trouvées par la méthode
x = linspace(Xstart,Xend,100)

#résolution exacte de l'équation
u = exp(-5*x)+x

#défintion de la fonction f (u' = f(x,u)) (avec la notation lambda)
f = _________

print(' ==================== Explicit 4th-order Runge Kutta ==========')

#on itère sur le nombre de pas de temps
for j in range(1,5):
    n = pow(2,j+1) # #nombre de pas de temps
    X = _________ #définir le vecteur temps
    h = _________ #définir le pas de temps
    U = zeros(n+1); U[0] = Ustart #initialiser le vecteur U

    #implémentation de la méthode de Runge Kutta d'ordre 4
    for i in range(n):
        _________
        _________
        _________
        _________
        _________

    #plots
    plt.subplot(2,2,j)
    plt.xlim((-0.1,4.1)); plt.ylim((-2.0,6.0)); plt.yticks(arange(-2,7,2))
    plt.plot(x,u,'-k',X,U,'.-b',markersize='5.0')
    print(' u(4) = %21.14e (Explicit 4th-order Runge Kutta with %2d steps )'% (U[-1],n))
plt.show()