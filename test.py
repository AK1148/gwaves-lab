import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.exp(x) * np.sin(x)

plt.plot(x, y)
plt.title("Test Plot: e^x * sin(x)")
plt.grid()
plt.show()
