import time
import numpy as np
from swarm import Swarm


class Drone:
    _id_counter = 0 # Class variable to keep track of next available ID
    all_drones = [] # List to store all created drones

    # Initialize parameters for a newly created drone
    def __init__(self, swarm, selfHeight=0):

        Drone._id_counter += 1

        # Initialise attributes
        self.swarm = swarm
        self._ID = Drone._id_counter
        self._selfHeight = selfHeight
        self._timeDelay = swarm.delays[self._ID-1] #Drone._id_counter
        self._ranges = np.full(swarm.numberDrones, np.nan)
        self._heights = np.full(swarm.numberDrones, np.nan)
        
        Drone.all_drones.append(self)

        # Set its height
        self._heights[self._ID-1]=selfHeight

    # This function will transmit data to the drone asking
    def transmit(self):

        print(f"Drone {self._ID} sending data: \n") # print to signify data transmission

        return self._selfHeight, self._ID # releases transmitting drones height and ID

    # This function wil recieve in data from other drones
    def recieveData(self, senderID, senderHeight, travelTimes):

        if (senderID!=self._ID):
            
            # Print signifies signal recieved
            print(f"Drone {self._ID} recieving data...")
            
            # Fill sender ID height into heights array
            self._heights[senderID-1] = senderHeight
            # Test print
            print(f"I am Drone {self._ID} and I believe drone {senderID} is at {self._heights[senderID-1]}\n")

    def returnSignal(self, senderID, travelTimes):
        time.sleep(self._timeDelay)
        if(senderID!=self._ID): 
            print(f"Drone {self._ID} sending a return signal to Drone {senderID} after {self._timeDelay} time units")
            delay=2*travelTimes[self._ID-1][senderID-1]+self._timeDelay
            return self._selfHeight, self._ID, delay

    def recieveReturnedData(self, returnedData):
        for i in range(len(self._heights)):
            if (i!= (self._ID-1)):
                self._heights[i]=returnedData[i]
        #print(f"\nDrone {self._ID}'s heights are: {self._heights}.\n")

    # Give the drone a height value
    def setSelfHeight(self, value):
        self._selfHeight=value
        self._heights[self._ID-1]=self._selfHeight


    def calculateRanges(self, totalTimes):
        for x in range(len(totalTimes)):
            oneWayTransitTime=(totalTimes[x]-self.swarm.delays[x])/2
            rangeToDrone=299702547*oneWayTransitTime
            self._ranges[x]=rangeToDrone

        return self._ranges

    """TEST FUNCTION"""
    def printInfo(self):
        print(f"Drone {self._ID}'s height is: {self._selfHeight}. It has a time delay of {self._timeDelay}")

# This function should collate the transmit, recieve, and return methods of the Drone class
def returnData(requestingDrone, travelTimes, swarm):

    # Initialize array to collate the times
    times = np.zeros((swarm.numberDrones, swarm.numberDrones), dtype=float)

    #Initialize array to collate all of the return signals
    returnedHeights = np.full(swarm.numberDrones, np.nan)

    tempHeight=0
    tempID=0

    # Transmit the data
    senderHeight, senderID = requestingDrone.transmit()

    # Record time transmitted
    transmitTime=time.time()

    # Recieve the data
    for drone in Drone.all_drones:
        drone.recieveData(senderID, senderHeight, travelTimes)

    #droneNum=1
    # Return the data

    delays=[]

    # Return the data
    for drone in Drone.all_drones:
        if drone!=requestingDrone:
            signalData = drone.returnSignal(senderID, travelTimes)
            if signalData:
                tempHeight, tempID, delay = signalData
            else:
                print("Error: data return\n")
                break
            returnedHeights[tempID-1]=tempHeight
            delays.append(delay)
        else:
            delays.append(-1)
            
            #times[senderID-1][droneNum-1]=transmitTime-time.time()
        #droneNum=droneNum+1
            
    #print(times)
        
    # Recieve returned data
    requestingDrone.recieveReturnedData(returnedHeights)

    distances=requestingDrone.calculateRanges(delays)
    return distances



"""

# Create drones
drone1 = Drone(selfHeight=6)
drone2 = Drone(selfHeight=4)
drone3 = Drone(selfHeight=8)
drone4 = Drone(selfHeight=10)


"""       