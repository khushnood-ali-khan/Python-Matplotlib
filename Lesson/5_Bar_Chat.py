import matplotlib.pyplot as plt
import numpy as np

subjects = np.array(["Proffesional Prictice", "OOAD", "Virtural system and service", "SNA", "Analysis of Algorithms"])
marks = np.array([73, 83, 81, 87, 89])

# BAR CHAT
# plt.bar(subjects, marks, color="skyblue")   # Vertical chat bar
plt.barh(subjects, marks, color="skyblue")   # Horizantal chat bar

plt.title("RESULT",
          fontsize=20,
          family="Arial",
          fontweight="bold",
          color="orange")

plt.xlabel("Subjects", fontsize=10, color="blue", fontweight="bold")
plt.ylabel("Marks", fontsize=10, fontweight="bold")

plt.show()