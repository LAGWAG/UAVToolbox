<<<<<<< HEAD
import math


print(math.sin(3*math.pi/2))
=======
import numpy as np

# Function to create a 2D array with given dimensions and initialize values
def create_2d_array(rows, cols, initial_value=0):
    return [[initial_value for _ in range(cols)] for _ in range(rows)]




"""COPY THIS"""
def extractCoordinates(threeDarray, frameNumber):
    xcoordinates=[]
    ycoordinates=[]
    for i in range(num_arrays):
        xcoordinates.append(threeDarray[i][frameNumber-1][0])
        ycoordinates.append(threeDarray[i][frameNumber-1][1])
    return xcoordinates, ycoordinates

# Number of 2D arrays
num_arrays = 3

# Dimensions of each 2D array
rows = 4
cols = 2

# Create a list of 2D arrays
list_of_2d_arrays = [create_2d_array(rows, cols, i + 1) for i in range(num_arrays)]

# Convert the list of 2D arrays to a 3D NumPy array
array_3d = np.array(list_of_2d_arrays)


# Accessing a specific element in the first array (for example, row=2, column=1)
element = array_3d[0, 1, 0]
print(f"Element at array_3d[0, 1, 0]: {element}")

array_3d[0] = np.arange(1, 9).reshape(4, 2)

# Creating the second array with increasing numbers
array_3d[1] = np.arange(10, 18).reshape(4, 2)

# Creating the third array with increasing numbers
array_3d[2] = np.arange(20, 28).reshape(4, 2)

# Print the 3D array
print("3D Array:")
print(array_3d)


# Print the 3D array
print("New 3D Array:")

print(array_3d[0][0][:])
print(array_3d[1][0][:])

x,y = extractCoordinates(array_3d, 1)

print(x)
print(y)


>>>>>>> acc3b8910839ce18f3ac88a40a1e555e97f5e074
