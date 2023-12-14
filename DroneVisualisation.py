import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
from svgpathtools import svg2paths
from svgpath2mpl import parse_path


def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

def generateCoordinates(nDrones):

    n=nDrones
    # Fixing random state for reproducibility
    np.random.seed(1908056)

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [0, 100], y in [0, 100], z in [zlow, zhigh].
    for m, zlow, zhigh in [('x', 0, 100)]:
        xs = randrange(n, 0, 100)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)

    return xs, ys, zs

def getTravelTimes(xs, ys, zs):
    n=len(xs)
    distances=np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            dx = xs[j] - xs[i]
            dy = ys[j] - ys[i]
            dz = zs[j] - zs[i]

            # Calculate the length of the line and store it
            length = np.sqrt(dx**2 + dy**2 + dz**2)
            distances[i][j]=length
    c=299702547 # m/s
    travelTimes=np.divide(distances, c)
    return travelTimes

def plotDrones(xs, ys, zs):

    n=len(xs)
    # Setup figure, axes, and close old plots
    plt.close('all')
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # SVG format
    uav_path, attributes = svg2paths('output.svg')
    uav_marker = parse_path(attributes[0]['d'])
    uav_marker.vertices-= uav_marker.vertices.mean(axis=0)

    ax.scatter(xs, ys, zs, color='grey', marker=uav_marker, s=1000, alpha=0.8)
    ax.scatter(xs, ys, zs, color='red', s=10, alpha=1)

    # initialise lengths
    lengths=[]

    # Connect each point with a double-ended arrow in blue
    for i in range(n):
        for j in range(i + 1, n):
            dx = xs[j] - xs[i]
            dy = ys[j] - ys[i]
            dz = zs[j] - zs[i]
            ax.quiver(xs[i], ys[i], zs[i], dx, dy, dz, color='black', arrow_length_ratio=0.2, linewidth=1, alpha=0.5, linestyle='dashed')

            # Calculate the length of the line and store it
            length = np.sqrt(dx**2 + dy**2 + dz**2)
            lengths.append(length)

            # Annotate the midpoint of the line with its length
            mid_x = (xs[i] + xs[j]) / 2
            mid_y = (ys[i] + ys[j]) / 2
            mid_z = (zs[i] + zs[j]) / 2
            ax.text(mid_x, mid_y, mid_z, f'L: {length:.1f}', fontsize=8, color='red')

    # Add coordinates caption
    for x, y, z in zip(xs, ys, zs):
        ax.text(x, y, z, f'({x:.1f}, {y:.1f}, {z:.1f})', fontsize=8, color='black')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    """ TESTING LINE """
    plt.show()
"""
xValues, yValues, zValues = generateCoordinates(4)
getTravelTimes(xValues, yValues, zValues)
#plotDrones([10,30,50,70], [20, 50, 80, 20], [10, 40, 80, 80])
plotDrones (xValues, yValues, zValues)
"""

def plotDrones2D(xs, ys, zs):
    n = len(xs)

    # Setup figure, axes, and close old plots
    plt.close('all')
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # SVG format
    uav_path, attributes = parse_path('output.svg')
    uav_marker = mpl.patches.PathPatch(uav_path, color='grey', alpha=0.8, lw=0)
    uav_marker.set_transform(ax.transData)

    ax.add_patch(uav_marker)
    ax.scatter(xs, ys, color='red', s=10, alpha=1)

    # Connect each point with a double-ended arrow in black
    for i in range(n):
        for j in range(i + 1, n):
            dx = xs[j] - xs[i]
            dy = ys[j] - ys[i]
            ax.quiver(xs[i], ys[i], dx, dy, color='black', arrow_length_ratio=0.2, linewidth=1, alpha=0.5, linestyle='dashed')

    # Add coordinates caption
    for x, y in zip(xs, ys):
        ax.text(x, y, f'({x:.1f}, {y:.1f})', fontsize=8, color='black')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')

    plt.show()