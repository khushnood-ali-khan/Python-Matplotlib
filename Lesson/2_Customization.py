import matplotlib.pyplot as plt
import numpy as np

arr1 = np.array([2021, 2022, 2023, 2024, 2025])
arr2 = np.array([40, 42, 47, 50, 60])

plt.plot(arr1, arr2, marker="o", #highlight each point with the given sign (. * v etc)
         # Change mark Size
         markersize=10,     # For Shortcut we can use ms=
         # Change Color
         markerfacecolor="red",     # For Shortcut we can use mfc=
         # Change edges Color
         markeredgecolor="yellow",      # For Shortcut we can use mec=

         # NOW styling line
         linestyle="dashed", # can use (dotted, dashdot, solid or none)
         #Change the line thickness
         linewidth=2,
         # Change line Color
         color="black")


plt.show()


""" 
    OKAY!, NOW! let say we have multiple lines in one plot, and we want to apply the same customization to the other lines too.
    one way to write every customization again but that would be messy, so we can just create a dictionary of the customization
    and unpack it in every line
"""

x = np.array([2021, 2022, 2023, 2024, 2025])
y1 = np.array([40, 42, 47, 50, 60])
y2 = np.array([34, 44, 56, 49, 51])

line_styling = dict(
    marker="*",
    markersize=15,
    markerfacecolor="blue",
    markeredgecolor="yellow",
    linestyle="dashdot",
    color="black",
    linewidth=2
)

plt.plot(x, y1, **line_styling)     # the double stars (**) unpack the dictonary
plt.plot(x, y2, **line_styling)

plt.show()

# A different color for each line we can pass the color in plot before unpacking dictonary
# plt.plot(x, y2, color="red" **line_styling)