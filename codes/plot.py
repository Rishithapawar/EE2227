import numpy as np
import matplotlib.pyplot as plt
l = np.linspace(-10,10,100)
L = []
M = []
X = []
Y=[]
def u(n):
    if (n >0):
        return 1
    else :
        return 0
def d(n):
    
    if (n==0):
        return 1
def x(n):
    return u(n)
def y(n):
    return -2/3*u(n) + 3/2*np.exp(-n)*u(n) - 5/6*np.exp(-3*n)*u(n)
def h(n):
    return -3/2*np.exp(-n)*u(n) + 5/2*np.exp(-3*n)*u(n)
def s(n):
    return -3/2*np.exp(-n)*u(n) + 5/2*np.exp(-3*n)*u(n)
def a(n):
    return 1

    
        
for i in l:
    L.append(x(i))
    M.append(y(i))
    X.append(h(i))
    Y.append(a(i))
plt.plot(l,L)

plt.plot(l,M)
plt.plot(l,X)
plt.plot(l,Y)


plt.legend(['y = x(t)','y = y(t)','y = h(t)','y= a(t)'],loc = 'upper left')
plt.show()
