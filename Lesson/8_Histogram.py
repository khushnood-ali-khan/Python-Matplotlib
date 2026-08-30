import matplotlib.pyplot as plt
import numpy as np

# Histogram Represents the data btw range

rng = np.random.default_rng()

data = np.array(rng.integers(50, 80, 20))

plt.hist(data, color="skyblue",
         # Define the no of pillors
         bins=10,
         # Add color to edge to see clearly
         edgecolor="black")

plt.title("RESULT", fontweight="bold", fontsize=20, color="orange")
plt.xlabel("Marks")
plt.ylabel("No of Students")

plt.show()