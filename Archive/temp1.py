import matplotlib as mpl

from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt

import numpy as np



# how many points to draw

points = 100



# generating x & y coordinates, their distance from origin,

# their angle relative to theeeeeeee origin, and random rotations to

# apply to each point each frame

xs = np.random.uniform(-1, 1, points)

ys = np.random.uniform(-1, 1, points)

ls = np.sqrt(xs**2 + ys**2)

angles = np.arctan2(ys, xs)

negs = np.random.choice([-1, 1], size=points)

rotations = (np.random.uniform(np.pi/50, np.pi/6, size=points) * negs)



# initialize a figure, make a color range to color each point

fig, ax = plt.subplots(figsize=(4,4))

ax.set_xlim(-1.5,1.5)

ax.set_ylim(-1.5,1.5)

color_divisions = [(1/points)*i for i in range(points)]

cmap = mpl.cm.get_cmap('jet')

colors = cmap(color_divisions)



# update function

# update gets fed elements from the frames parameter of FuncAnimation

# each update we clear the graph (but reapply the same x/y limits)

# we then 