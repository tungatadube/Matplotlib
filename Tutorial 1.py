import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
#red dashes, blue squares, green triangles
plt.plot(t, t, 'r-.', t,t**2, 'bs', t, t**3, 'g^', t, t**3.1, 'r--')
plt.ylabel('some digits')
plt.xlabel('the digits')
plt.title('Varience')
plt.show()
