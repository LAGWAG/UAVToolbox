import numpy as np

n = 5  # Replace 5 with the number of drones you have

drone_array = np.array(["drone{}".format(i) for i in range(1, n+1)]).reshape(-1, 1)

# If you are using Python 3.6 or above, you can use f-strings for a more concise syntax:
# drone_array = np.array([f"drone{i}" for i in range(1, n+1)]).reshape(-1, 1)

print(drone_array)