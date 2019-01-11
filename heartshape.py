import matplotlib.pyplot as plt
import numpy as np

# create x and y co-ordinates
t = np.arange(0, 2 * np.pi, 0.1)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5*np.cos(2*t) - 2 * np.cos(3*t)-np.cos(4*t)

# disable axis lines
plt.axis('off')

# set outer line of insert
# disable the below line if you don't want the outer line
# choose different color by changing the color codes
plt.plot(x, y, color = '#FFC0CB', linewidth = 7.0)

# fill liner part of heart
plt.fill(x, y, color='#FFB6C1')

#finally <3
plt.show()
