import numpy as np

class Swarm: 


    def __init__(self, numberDrones):
        self.numberDrones=numberDrones
        self.delays=np.arange(numberDrones)

#swarm=Swarm(4)
        