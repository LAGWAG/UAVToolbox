import math

def calculate_true_bearing(x0, y0, x1, y1):
    # Calculate the differences in coordinates
    dx = x1 - x0
    dy = y1 - y0

    # Calculate the true bearing using arctangent
    true_bearing_rad = math.atan2(dy, dx)

    # Convert radians to degrees and normalize to the range [0, 360)
    true_bearing_deg = math.degrees(true_bearing_rad) % 360

    return true_bearing_deg

# Example usage:
x0, y0 = 0, 0  # Starting point
x1, y1 = 3, 4  # Destination point

bearing = calculate_true_bearing(x0, y0, x1, y1)
print(f'True Bearing from ({x0}, {y0}) to ({x1}, {y1}): {bearing} degrees')
