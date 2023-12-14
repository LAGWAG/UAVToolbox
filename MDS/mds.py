import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import ConnectionPatch
from scipy.spatial.distance import euclidean

def mds(D):
  #D = np.loadtxt('distances.txt', delimiter=',')
  #C = np.genfromtxt('cities.txt', dtype = 'str', delimiter="\n")
  n = len(D)
  C = np.array([f"Drone{i}" for i in range(1, n+1)]).reshape(-1, 1)

  H = np.eye(n) - np.ones((n,n))/n
  B = -0.5 * H.dot(D**2).dot(H)
 
  evals, evecs = np.linalg.eigh(B)
  idx = np.argsort(evals)[::-1]
  evals = evals[idx]
  evecs = evecs[:,idx] # col i represents eigenvector i

  #w, = np.where(evals > 0)
  w = [0,1]
  L = np.diag(np.sqrt(evals[w]))
  U = evecs[:,w]
  Y = U.dot(L)
  return Y, C

def annotate_distance(ax, point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    # Draw a line between the points
    line = ConnectionPatch((x1, y1), (x2, y2), 'data', 'data', arrowstyle="-", linewidth=0.5, color='gray')
    ax.add_artist(line)

    # Calculate distance
    distance = euclidean(point1, point2)

    # Annotate the line with the distance
    text_x = (x1 + x2) / 2
    text_y = (y1 + y2) / 2
    ax.text(text_x, text_y, f'{distance:.2f}', ha='center', va='center', color='blue', fontsize=8)

def annotate_point(ax, point, label):
    x, y = point
    ax.text(x, y, label, ha='center', va='bottom', color='black', fontsize=8)

def plot(Y, C, d):
  fig = plt.figure(0)
  ax = fig.add_subplot(111)
  ax.set_title('Original Plot')
  ax.set_xlabel('X-axis')
  ax.set_ylabel('Y-axis')
  ax.grid(True, linestyle='--', alpha=0.7)
  ax.scatter(Y[:,0], Y[:,1])
  #or i in range(len(C)):
    #ax.annotate(C[i], (Y[i][0], Y[i][1]+20), fontsize = 10)

  # Annotate distances between points
  for i in range(len(Y)):
      for j in range(i + 1, len(Y)):
          annotate_distance(ax, Y[i], Y[j])

  # Annotate each point with its point number
  for i in range(len(C)):
      annotate_point(ax, (Y[i][0], Y[i][1]), str(i + 1))

  plt.savefig('hw7-4.pdf')
  """
  fig1 = plt.figure(1)
  theta = d / 180.0 * math.pi
  R = np.array([[math.cos(theta), -math.sin(theta)],[math.sin(theta), math.cos(theta)]])
  Y_t = R.dot(Y.T).T
  ax1 = fig1.add_subplot(111)
  ax1.scatter(Y_t[:,0], Y_t[:,1])
  #for i in range(len(C)):
    #ax1.annotate(C[i], (Y_t[i][0], Y_t[i][1]+20), fontsize = 10)

  # Annotate each point with its point number
  for i in range(len(C)):
    annotate_point(ax1, (Y_t[i][0], Y_t[i][1]), str(i + 1))

  # Annotate distances between points
  for i in range(len(Y_t)):
      for j in range(i + 1, len(Y_t)):
          annotate_distance(ax1, Y_t[i], Y_t[j])
  
  plt.savefig('hw7-4_turn.pdf')
"""
def main(D):
  Y, C = mds(D)
  plot(Y, C, -90)
