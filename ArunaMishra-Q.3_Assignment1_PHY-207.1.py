#Name: Aruna Mishra
#Batch: PhD 2025
#Q.3, Assignment I, PHY-207.1

import matplotlib.pyplot as plt
import numpy as np

c = 3 * (10**8)    #speed of light
def gamma(v):
    return((1-((v*v)/(c*c)))**(-0.5))       #calculating gamma

o = np.linspace(0.01*c, 0.9999*c, 1000)

s = np.array('d', )
s = [0.0 for u in range(1000)]

for i in range(1000):
    s[i] = o[i]

gamma_evaluate = np.array('d', )
gamma_evaluate = [0.0 for u in range(1000)]

for i in range(1000):
    gamma_evaluate[i] = gamma(s[i])

plt.plot(s, gamma_evaluate, color = 'red')        #plot of gamma as a function of v
plt.xlabel("v")
plt.ylabel(r'$\gamma = T/\tau$')
plt.title(r'T/$\tau = \gamma$ as a function of velocity v of the particle (Q.3)')
plt.show()