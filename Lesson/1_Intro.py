import matplotlib.pyplot as plt

# Basic Plot
x = [2023, 2024, 2025, 2026]
y = [1000, 1500, 1200, 1800]

plt.plot(x, y)
plt.show()

# we can use numpy array since they are faster then ppython list
import numpy as np

x_axis = np.array([1, 2, 3, 4, 5, 6])
y_axis = np.array([3.6, 3.5, 3.3, 3.5, 3.7, 3.8])

plt.plot(x_axis, y_axis)
plt.show()