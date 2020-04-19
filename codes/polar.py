import control
import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(-20,20,2000)

num=[1]
den=[1,6,11,7]

G = control.tf(num,den)
magnitude, phase, W = G.freqresp(omega)

ax1 = plt.subplot(111, projection='polar')
ax1.plot(phase.reshape((2000,))[-1000:],magnitude.reshape((2000,))[-1000:])
plt.title("polar plot")
plt.savefig('polar.png')
plt.show()
