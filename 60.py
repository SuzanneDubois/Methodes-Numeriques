import matplotlib.pyplot as plt
from numpy import *

x,y = meshgrid(linspace(-3,3,1000),linspace(-3,3,1000))

z = x + 1j*y #définition d'un nombre complexe

#trouver équation second degré de a
b = 1 + z + 3*z*z/4
c = z*z/4.0

#résolution equation second degré
f1 = abs(b - sqrt(b*b - 4*c))/2
f2 = abs(b + sqrt(b*b - 4*c))/2
gain = maximum(f1,f2)

#plot avec coutour max en 1
plt.contourf(x,y,gain,arange(0,1.1,0.1),cmap=plt.cm.jet_r)
plt.contour(x,y,gain,arange(0,1.1,0.1),colors='black')
ax = plt.gca()
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
ax.yaxis.grid(color='gray',linestyle='dashed')
ax.xaxis.grid(color='gray',linestyle='dashed')
plt.xticks(arange(-3,4,1))
plt.yticks(arange(-3,4,1))
plt.show()