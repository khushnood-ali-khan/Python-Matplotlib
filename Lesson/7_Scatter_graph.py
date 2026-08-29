import matplotlib.pyplot as plt
import numpy as np

# Shows the relation btw to variables, Helps to identify a correlation (+, -, or none) (like directly, or indirectly proportional)
rng = np.random.default_rng()

#   1st data set
T1_over = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
T1_runs = np.array(rng.integers(0, 25, 10))

#   2st data set
T2_over = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
T2_runs = np.array(rng.integers(0, 25, 10))

plt.scatter(T1_over, T1_runs,
            # Opacity
            alpha= 0.5,
            # Size
            s = 50,
            # Label
            label="Team 1"
            )

plt.scatter(T2_over, T2_runs, color="red",
            # Opacity
            alpha= 0.5,
            # Size
            s = 50,
            # Label
            label="Team 2"
            )


plt.title("Performance Chart", fontsize=20, color="green", fontweight="bold")
plt.xlabel("Overs", fontsize=12)
plt.ylabel("Runs", fontsize=12)
plt.xticks(T1_over)

#   each satter presentation
plt.legend()

plt.show()