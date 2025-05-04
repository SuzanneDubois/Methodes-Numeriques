from math import exp
f = lambda x : x*exp(x) #equation a résoudre
dfdx = lambda x : (x + 1.0)*exp(x) #fonction dérivée

def newton(x,tol,nmax):
    n = 0; delta = float("inf")
    while ((abs(delta) > tol) and (n < nmax)) : # bérifier la condition d'arrêt
        delta = -f(x) / dfdx(x) #appliquer la méthode de Newton raphson
        x = x + delta
        n = n + 1
        print(" x = %14.7e (Estimated error %13.7e at iteration %d)"% (x,abs(delta),n))
    return x

print("Found x = %14.7e" % newton( 0.2,1e-13,50))
print("Found x = %14.7e" % newton(20.0,1e-13,50)) 
