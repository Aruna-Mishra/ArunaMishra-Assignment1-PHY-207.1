#Name: Aruna Mishra
#Batch: PhD 2025
#Q.1, Assignment I, PHY-207.1

import math
import matplotlib.pyplot as plt
import numpy as np

#Plotting the extra term obtained in the Galilean transformation of Gauss Law
#Taking B = z in the y direction
#Taking v = v in the x direction
#v x B = vz in the z direction
#del.(vz in z direction) = v
#Hence plotting v as a function of v

c = 3 * (10**8)    #speed of light

x = np.linspace(0.01*c, 0.9999*c, 1000)
y = x

plt.plot(x, y, color = 'red', label = r'Plotting the extra term obtained in the Galilean transformation of Gauss Law; Taking B = z in the y direction; Taking v = v in the x direction; v x B = vz in the z direction; $\nabla$.(vz in z direction) = v; Hence plotting v as a function of v')
plt.xlabel("v")
plt.ylabel("Difference in result")
plt.title('Difference in result as a function of velocity value v (Q.1)')
plt.legend(fontsize='small',loc=(-0.07,1.07))
plt.show()


