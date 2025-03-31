import matplotlib.pyplot as plt
from numpy import *

x,y = meshgrid(linspace(-3,3,1000),linspace(-3,3,1000))

z = x + 1j*y #définition d'un nombre complexe

#trouver équation second degré de a
b = _________
c = _________

#résolution equation second degré
f1 = _________
f2 = _________
gain = maximum(f1,f2)

#plot avec coutour max en 1
plt.contourf(x,y,gain,arange(_________),cmap=plt.cm.jet_r)
plt.contour(x,y,gain,arange(_________),colors='black')
ax = plt.gca()
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
ax.yaxis.grid(color='gray',linestyle='dashed')
ax.xaxis.grid(color='gray',linestyle='dashed')
plt.xticks(arange(-3,4,1))
plt.yticks(arange(-3,4,1))
plt.show()