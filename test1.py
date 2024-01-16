import matplotlib.pyplot as plt
import numpy as np

# Creating arrays with increasing numbers
array1 = np.arange(1, 9).reshape(4, 2)
array2 = np.arange(10, 18).reshape(4, 2)
array3 = np.arange(20, 28).reshape(4, 2)

# Concatenating the arrays into a single array
all_arrays = np.vstack((array1, array2, array3))

# Creating a scatter plot
plt.scatter(all_arrays[:, 0], all_arrays[:, 1])

# Annotating each point with its point number
for i, point in enumerate(all_arrays):
    plt.annotate(f"{i+1}", (point[0], point[1]), textcoords="offset points", xytext=(5,5), ha='center')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Annotations')

# Displaying the plot
plt.show()