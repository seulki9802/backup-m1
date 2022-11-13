import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

x = np.arange(-6, 6, 0.01)
y = 1 / (1 + np.exp(x))
y2 = 1 / (1 + np.exp(-x))

plt.plot(x, y)
plt.plot(x, y2)
plt.legend()
plt.show()