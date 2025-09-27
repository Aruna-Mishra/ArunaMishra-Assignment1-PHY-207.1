#Name: Aruna Mishra
#Batch: PhD 2025
#Q.2(a), Assignment I, PHY-207.1

import math
import matplotlib.pyplot as plt
import numpy as np

c = 3 * (10**8)    #speed of light

v = 0
psi = math.atanh(v/c) #angle of rotation
m_x = math.tan(psi)
m_ct = math.tan((math.pi/2) + psi)
x = np.linspace(-100, 100, 100)
xaxis_prime = m_x * x
ctaxis_prime = m_ct * x
plt.plot(x, xaxis_prime, color = 'black',label='ct-x when v = 0')
plt.plot(x, ctaxis_prime, color = 'black')

v = 0.01*c
psi = math.atanh(v/c) #angle of rotation
m_x = math.tan(psi)
m_ct = -1/m_x
x = np.linspace(-100, 100, 100)
xaxis_prime = m_x * x
ctaxis_prime = m_ct * x
plt.plot(x, xaxis_prime, color = 'yellow', label=" ct'-x' when v = 0.01c ")
plt.plot(x, ctaxis_prime, color = 'yellow')

v = 0.5*c
psi = math.atanh(v/c) #angle of rotation
m_x = math.tan(psi)
m_ct = -1/m_x
x = np.linspace(-100, 100, 100)
xaxis_prime = m_x * x
ctaxis_prime = m_ct * x
plt.plot(x, xaxis_prime, color = 'red', label=" ct'-x' when v = 0.5c ")
plt.plot(x, ctaxis_prime, color = 'red')

v = 0.9999*c
psi = math.atanh(v/c) #angle of rotation
m_x = math.tan(psi)
m_ct = -1/m_x
x = np.linspace(-100, 100, 100)
xaxis_prime = m_x * x
ctaxis_prime = m_ct * x
plt.plot(x, xaxis_prime, color = 'green', label=" ct'-x' when v = 0.9999c ")
plt.plot(x, ctaxis_prime, color = 'green')


plt.xlim(-100, 100)
plt.ylim (-100, 100)
axis = plt.gca()
plt.xlabel("x'")
plt.ylabel("ct'")
plt.title(r'Space-time diagram for different velocity values (Q.2(a))')
plt.legend()
plt.show()

