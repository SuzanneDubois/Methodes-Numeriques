import numpy as np
import matplotlib.pyplot as plt

def Euler_explicite(start,end,n):
    h = (end-start)/n
    X = np.linspace(start,end,n+1)
    U = np.empty(n+1); U[0] = 0

    for i in range(0,n):
        U[i+1] = U[i] + h * (np.sin(X[i]) + U[i])
    
    return X,U

def Euler_implicite(start,end,n):
    h = (end-start)/n
    X = np.linspace(start,end,n+1)
    U = np.empty(n+1); U[0] = 0

    for i in range(0,n):
        U[i+1] = (U[i] + h * np.sin(X[i+1]))/(1-h)
    
    return X,U

start = 0; end = 1; n = 100 # en changeant n observez que l'erreur diminue en O(n) !!!
X = np.linspace(start,end,n+1)
U = np.empty(n+1)
for i in range(n+1):
    U[i] = 0.5*(np.exp(X[i]) - np.sin(X[i]) - np.cos(X[i]))
Xe, Ue = Euler_explicite(start,end,n)
Xi, Ui = Euler_implicite(start,end,n)

#valeur de u(1) :
print("Vraie valeur de u(1)                         : ", U[-1])
print("Valeur approchée de u(1) par Euler explicite : ", Ue[-1], "erreur : ", abs(Ue[-1] - U[-1]))
print("Valeur approchée de u(1) par Euler implicite : ", Ui[-1], "erreur : ", abs(Ui[-1] - U[-1]))

plt.plot(X,U,label="exact")
plt.plot(Xe,Ue,label="Euler explicite")
plt.plot(Xi,Ui,label="Euler implicite")
plt.legend()
plt.show()
 

# note : convergence linéaire, cela signifie que quand n est augmenté 
# d'un facteur 10, l'erreur diminue d'un facteur 10. Vérifiez avec les décimales !!