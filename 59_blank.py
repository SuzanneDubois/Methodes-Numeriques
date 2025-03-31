from numpy import *
from matplotlib import pyplot as plt

#défintion de la fonction f
def f(x,u):
    L = 20; k2 = 9.81/L; phi = pi/2; omega = 7.29e-05
    dudx = zeros(4) 
    dudx[0] = _________
    dudx[1] = _________
    dudx[2] = _________
    dudx[3] = _________
    return dudx

Xstart = 0; Xend = 300 #définir l'intervalle de temps
Ustart = [1,0,0,0] #définir les conditions initiales
print("==== Using explicit Euler integrator :-(")

n = 30000 #nombre de pas de temps
X = _________ #définir le vecteur temps
U = _________; U[0] = _________ #initialiser le vecteur U 
h = (Xend - Xstart)/n #définir le pas de temps

#intégration explicite d'Euler
for i in range(n):
    _________ #implémzntation de la méthode d'Euler explicite

#tracer le résultat
print(" number of steps used : %d " % n)
plt.figure(); plt.xlim((-2.00, 2.00)); plt.ylim((-0.05, 0.05))
plt.plot(U[:,0],U[:,1],'-r')
plt.title("Explicit Euler")
plt.show()


#Est-ce que le résultat est correct ? Changez Xend et regardez le résultat, est ce physiquement correct ?

print("==== Using RK23 integrator from scipy :-)")
from scipy.integrate import solve_ivp
sol = solve_ivp(f,[Xstart,Xend],Ustart, method='RK23')

print(" number of steps used : %d " % len(sol.t))
plt.figure(); plt.xlim((-2.00, 2.00)); plt.ylim((-0.05, 0.05))
plt.plot(sol.y[2], sol.y[3], '-b')
plt.show()