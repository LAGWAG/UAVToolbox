import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class UAV:
    def __init__(self, start_position):
        self.position = np.array(start_position, dtype=float)
        self.waypoint = None
        self.speed = 0.1  # Adjust the speed of the UAV

    def set_waypoint(self, waypoint):
        self.waypoint = np.array(waypoint, dtype=float)

    def update_position(self):
        if self.waypoint is not None:
            direction = self.waypoint - self.position
            distance = np.linalg.norm(direction)
            if distance > self.speed:
                # Normalize direction and move towards the waypoint
                self.position += (direction / distance) * self.speed
            else:
                # Reached the waypoint
                self.position = self.waypoint
                self.waypoint = None

# Create a UAV instance
uav = UAV(start_position=(0, 0))

# Set the waypoint for the UAV
waypoint = (5, 5)
uav.set_waypoint(waypoint)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)

# Create a point representing the UAV
uav_point, = ax.plot([], [], 'ro', markersize=10)

# Create a point representing the waypoint
waypoint_point, = ax.plot([], [], 'bo', markersize=10)

# Create a static point at (5, 5)
static_point, = ax.plot([], [], 'go', markersize=10)

# Function to initialize the plot
def init():
    uav_point.set_data([], [])
    waypoint_point.set_data(*waypoint)
    static_point.set_data(*waypoint)  # Display the static point
    return uav_point, waypoint_point, static_point

# Function to update the plot in each frame
def update(frame):
    uav.update_position()
    uav_point.set_data([uav.position[0]], [uav.position[1]])  # Pass data as a list
    return uav_point,

# Create the animation
animation = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)

# Show the animation
plt.show()
