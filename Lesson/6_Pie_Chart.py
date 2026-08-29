import matplotlib.pyplot as plt
import numpy as np

earth = ["Ocean", "Land"]
percentage = np.array([71, 29,])

colors = ["skyblue", "lightgreen"]

plt.pie(percentage, labels=earth,
        # ADD Percentage
        autopct="%1.1f%%",
        # ADD color to each slice
        colors=colors,
        # Hightlight a Slice
        explode=[0, 0.1],    # value higher then 0 is for highlighted one
        # Shadow the pie chart
        shadow=True,
        # Rotate the chart
        startangle=180      #rotate 180 degree
        )

plt.title("Earth", fontweight="bold", fontsize=15)

plt.show()