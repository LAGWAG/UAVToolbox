import DroneRanging
import DroneVisualisation
import swarm
import numpy as np

# number of Drones
numberDrones=4

# Generate coordinates for n drones
xValues, yValues, zValues = DroneVisualisation.generateCoordinates(numberDrones)

# Get the travel times for RF between the drones
TravelTimes=DroneVisualisation.getTravelTimes(xValues, yValues, zValues)

# Create swarm with certain number of drones
swarm1=swarm.Swarm(numberDrones)

drones=[]

for i, z in enumerate(zValues):
    drone = DroneRanging.Drone(selfHeight=z, swarm=swarm1)
    drones.append(drone)

# Performs the echo from (drone)
rangesFrom1=DroneRanging.returnData(drones[0], TravelTimes, swarm1)
print(f"\nDrone 1 sees the other drones at the following distances: {rangesFrom1[1:]}")

# Plot
DroneVisualisation.plotDrones(xValues, yValues, zValues)