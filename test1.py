import numpy as np

# Function to create a 2D array with given dimensions and initialize values
def create_2d_array(rows, cols, initial_value=0):
    return [[initial_value for _ in range(cols)] for _ in range(rows)]

# Number of 2D arrays
num_arrays = 3

# Dimensions of each 2D array
rows = 4
cols = 3

# Create a list of 2D arrays
list_of_2d_arrays = [create_2d_array(rows, cols, i + 1) for i in range(num_arrays)]

# Convert the list of 2D arrays to a 3D NumPy array
array_3d = np.array(list_of_2d_arrays)

# Print the 3D array
print("3D Array:")
print(array_3d)

# Accessing a specific element in the first array (for example, row=2, column=1)
element = array_3d[0, 1, 0]
print(f"Element at array_3d[0, 1, 0]: {element}")

array_3d[0]=np.array([[19, 20, 21], [22, 23, 24], [25, 26, 27],[28, 29, 30]])

# Print the 3D array
print("New 3D Array:")
print(array_3d)