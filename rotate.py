import numpy as np

def rotate_points(Y, center_point, angle_degrees):
    """
    Rotate a set of points Y about a given center_point by a specified angle in degrees.

    Parameters:
    - Y: numpy array of shape (n, 2), representing the set of points to be rotated.
    - center_point: tuple or list of length 2, representing the center point of rotation.
    - angle_degrees: float, the angle in degrees by which to rotate the points.

    Returns:
    - rotated_points: numpy array of shape (n, 2), representing the rotated points.
    """

    # Convert angle to radians
    angle_radians = np.radians(angle_degrees)

    # Translate the points so that the center_point becomes the origin
    Y_translated = Y - center_point

    # Perform rotation
    rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                               [np.sin(angle_radians), np.cos(angle_radians)]])
    rotated_points = np.dot(Y_translated, rotation_matrix)

    # Translate the points back to their original position
    rotated_points += center_point

    return rotated_points

# Example usage:
#Y = np.array([[1, 2], [3, 4], [5, 6]])  # Replace with your set of points
#center_point = [1, 1]  # Replace with your desired center point
#angle_degrees = 45.0  # Replace with your desired rotation angle
#rotated_points = rotate_points(Y, center_point, angle_degrees)
#print(rotated_points)
