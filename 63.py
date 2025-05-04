from cmath import sqrt
f = lambda x : 2*sqrt(x-1)
def iter(x,tol,nmax):
    n = 0; delta = float("inf")
    while ((abs(delta) > tol) and (n < nmax)) :
        xold = x
        x = f(x)
        delta = x - xold
        n = n + 1
        print(" x = %05f%+05fi (Estimated error %13.7e at iteration %d)"% (x.real,x.imag,abs(delta),n))
    return x

print("Found x = ", iter(1.5,1e-2,50))
print("Found x = ", iter(2.5,1e-2,50))