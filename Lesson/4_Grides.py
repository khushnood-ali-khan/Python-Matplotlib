import matplotlib.pyplot as plt
import numpy as np

# GIRDE FUNCTION HELP US UNDERSTAND THE DATA

x = np.array([1, 2, 3, 4, 5])
y = np.array([30, 20, 15, 45, 60])

plt.grid(axis="x", # can pass x, y, or both
         linewidth=2,
         color="red",
         linestyle="dotted")

plt.plot(x,y, marker="o", markersize=10)
plt.xticks(x)
plt.show()