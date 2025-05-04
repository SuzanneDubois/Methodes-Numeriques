# -------------------------------------------------------------------------
#
# PYTHON for SCIENTIFIC COMPUTING
# April 2020 : ex 73 (exam of June 2003)
#
#  Vincent Legat
#
# -------------------------------------------------------------------------
#

from numpy import *
from numpy.linalg import solve,norm

from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['toolbar'] = 'None'
fig = plt.figure("Non-linear approximation : u(x) = a/(x+b)")


X = array([ 0.0, 1.0, 2.0])
U = array([49/8, 2.0,25/8])
x = linspace(-0.5,3,100)

alpha = array([5.5,0.8])
nmax = 30; iter = 0; tol = 1e-8; dalpha = 1
error = zeros(nmax)
while (iter < nmax) and (norm(dalpha) > tol):

  a = alpha[0]
  b = alpha[1]
  R    = (U - a/(X+b))
  dRda = -1/(X+b)
  dRdb =  a/(X+b)**2
  dRdaa = 0
  dRdab = 1/(X+b)**2
  dRdbb = -(2*a)/(X+b)**3
    
  F = sum(R*R); dF = zeros(2); ddF = zeros((2,2))
  dF[0] = 2 * sum(R*dRda)
  dF[1] = 2 * sum(R*dRdb)
  ddF[0,0] = 2 * sum(dRda*dRda + R * dRdaa)
  ddF[0,1] = 2 * sum(dRdb*dRda + R * dRdab)           
  ddF[1,0] = ddF[0,1]
  ddF[1,1] = 2 * sum(dRdb*dRdb + R * dRdbb)

  dalpha = -solve(ddF,dF)
  alpha = alpha + dalpha
  error[iter] = norm(dalpha)
  iter = iter + 1
  print('   Iteration %i : %14.7e (a =%14.7e b =%14.7e)' % (iter,norm(dalpha),alpha[0],alpha[1]))
  u = alpha[0]/(x + alpha[1])
  plt.plot(x,u,'-b',linewidth = 0.5)

if (iter > 1) :
  rate = mean(log(error[1:iter])/log(error[:iter-1]))
  print('   Observed rate of convergence : %.2f ' % rate)
  print('   Theoretical rate             : %.2f ' % 2.0)

  

u = alpha[0]/(x + alpha[1])
plt.plot(x,u,'-r')
plt.plot(X,U,'or')
plt.show()




