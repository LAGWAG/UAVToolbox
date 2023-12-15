import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points (n)
n = 2

# Define the number of drones
m = 3

# Generate four arrays of size n x 2 representing (x, y) points and put them into a list
np.random.seed(10)
point_list = [100*np.random.rand(m, 2) for _ in range(n)]
print(point_list[0])

# Create a scatter plot with no points initially
fig, ax = plt.subplots()
scatter = ax.scatter([], [], marker='o')

# Set the axis limits
ax.set_xlim(0, 105)
ax.set_ylim(0, 105)

# Generate a list of unique colors for each point
colors = ['b', 'g', 'r', 'y']

# Update function for animation
def update(frame):
    x_values = [point[frame % m, 0] for point in point_list]
    y_values = [point[frame % m, 1] for point in point_list]
    scatter.set_offsets(np.column_stack((x_values, y_values)))

    # Assign a unique color to each point
    scatter.set_color(colors[frame % len(colors)])
    
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=n, interval=1000, blit=True)

plt.show()
