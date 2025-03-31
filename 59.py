from numpy import *
from matplotlib import pyplot as plt

#défintion de la fonction f
def f(x,u):
    L = 20; k2 = 9.81/L; phi = pi/2; omega = 7.29e-05
    dudx = zeros(4) #on a 4 equations dans le système donc un vecteur de fonctions de taille 4 [x,y,u,v]
    dudx[0] = u[2]  #x' = u
    dudx[1] = u[3] #y' = v
    dudx[2] = 2*omega*sin(phi)*u[3] - k2*u[0] #u' = 2*omega*sin(phi)*v - k2*x
    dudx[3] = -2*omega*sin(phi)*u[2] - k2*u[1] #v' = -2*omega*sin(phi)*u - k2*y
    return dudx

Xstart = 0; Xend = 300 #définir l'intervalle de temps
Ustart = [1,0,0,0] #définir les conditions initiales
print("==== Using explicit Euler integrator :-(")

n = 30000 #nombre de pas de temps
X = linspace(Xstart,Xend,n+1) #définir le vecteur temps
U = zeros((n+1,4)); U[0] = Ustart #initialiser le vecteur U 4 X le nombre de pas de temps
h = (Xend - Xstart)/n #définir le pas de temps

#intégration explicite d'Euler
for i in range(n):
    U[i+1,:] = U[i,:] + h*f(X[i],U[i,:]) #implémzntation de la méthode d'Euler explicite

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