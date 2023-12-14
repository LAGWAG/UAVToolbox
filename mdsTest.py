import DroneRanging
import DroneVisualisation
import swarm
import numpy as np
import MDS.mds as mds
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation

# Close all previously open plots
plt.close('all')

# number of Drones
numberDrones=4
c=299702547


# Generate coordinates for n drones
xValues, yValues, zValues = DroneVisualisation.generateCoordinates(numberDrones)

zValues=[0,0,0,0]
# Get the travel times for RF between the drones
d=np.multiply(DroneVisualisation.getTravelTimes(xValues, yValues, zValues), c)

# Store min and max x values for later
minX, maxX=min(xValues), max(xValues)
minY, maxY=min(yValues), max(yValues)

mds.main(d)
# Create swarm with certain number of drones
swarm1=swarm.Swarm(numberDrones)

drones=[]

# Create drones
for i, z in enumerate(zValues):
    drone = DroneRanging.Drone(selfHeight=0, swarm=swarm1)
    drones.append(drone)

# Plot
#DroneVisualisation.plotDrones2D(xValues, yValues, zValues)

def annotateDistance(ax, point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Draw a dotted line between the points
    ax.plot([x1, x2], [y1, y2], 'k--', alpha=0.5)

    # Calculate distance
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Annotate the midpoint of the line with the distance
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    ax.text(mid_x, mid_y, f'{distance:.2f}', ha='center', va='center', color='blue')

def annotate_point(ax, point, label):
    x, y = point
    ax.text(x, y, f'{label}', ha='center', va='bottom', color='black')


# Plot the points
fig, ax = plt.subplots()
scatter = ax.scatter(xValues, yValues, color='red', s=50)
# Annotate distances between points
for i in range(len(xValues)):
    for j in range(i + 1, len(xValues)):
        annotateDistance(ax, (xValues[i], yValues[i]), (xValues[j], yValues[j]))

# Annotate each point with its point number
for i, point in enumerate(zip(xValues, yValues), start=1):
    annotate_point(ax, point, str(i))

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Annotating Distances between Points')

def update(frame):
    #global xValues, yValues

    # Clear the Axes to remove previous elements
    ax.clear()

    # Plot the points
    scatter = ax.scatter(xValues, yValues, color='red', s=50)
    yValues[0] += 1

    # Set the limits of the axes to keep the window the same
    ax.set_xlim(minX-10,maxX+10)
    ax.set_ylim(minY-10, maxY+10)

    # Copying from above
    
    # Annotate distances between points
    for i in range(len(xValues)):
        for j in range(i + 1, len(xValues)):
            annotateDistance(ax, (xValues[i], yValues[i]), (xValues[j], yValues[j]))

    # Annotate each point with its point number
    for i, point in enumerate(zip(xValues, yValues), start=1):
        annotate_point(ax, point, str(i))


    scatter.set_offsets(np.column_stack((xValues, yValues)))
    return scatter,

animation = animation.FuncAnimation(fig, update, frames=10, interval=1000, blit=True)

plt.show()