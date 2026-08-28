import matplotlib.pyplot as plt
import numpy as np

x = np.array([2021, 2022, 2023, 2024, 2025])
y = np.array([69000, 48000, 42000, 108000, 126000])

# Labels
    # TITLE
plt.title("BITCOIN PEAK PRICES",
          #TEXT SIZE
          fontsize=15,
          # CHANGE family
          family="Arial",
          # Font weight
          fontweight="bold",
          # COLOR
          color="orange")

# X-Axies Label
plt.xlabel("Year",
           fontsize=12,
           fontweight="bold")

# Y-Axies Label
plt.ylabel("$ Price",
           fontsize=12,
           fontweight="bold",
           color="blue")

# CHANGE THE X and Y Axies Ticks
plt.tick_params(axis="both", #can put x, y or both
                color="red")

plt.plot(x,y, marker="o", markersize=5)

# The Year on the x-axies looks like, 2021.5 2022.0, so to fix that we can use xticks() or yticks()
plt.xticks(x)       # now it will looks as it is x array

plt.show()