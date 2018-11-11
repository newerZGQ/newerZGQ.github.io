import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,4,0,2])
plt.xlabel("τ")

X = np.linspace(np.pi/6, np.pi, 256, endpoint = True)
A = 0.5*np.cos(3 * X) + 1
plt.plot(X,A)
plt.plot([1.5,3.5],[0.2,1])

plt.text(2.2,1.5,"f(τ)",fontsize = 15)
plt.text(3.5,1.1,"h(t-τ)",fontsize = 15)

plt.show()
