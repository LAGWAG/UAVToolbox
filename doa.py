import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

################################################
# SIMULATE SIGNAL
################################################

sample_rate = 1e6
N = 10000 # number of samples to simulate

# Create a tone to act as the transmitter signal
t = np.arange(N)/sample_rate # time vector
f_tone = 0.02e6
tx = np.exp(2j * np.pi * f_tone * t)

d = 0.5 # half wavelength spacing
Nr = 3
theta_degrees = 20 # direction of arrival (feel free to change this, it's arbitrary)
theta = theta_degrees / 180 * np.pi # convert to radians
a = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta)) # array factor
print(a) # note that it's 3 elements long, it's complex, and the first element is 1+0j

a = a.reshape(-1,1)
print(a.shape) # 3x1
tx = tx.reshape(-1,1)
print(tx.shape) # 10000x1

# matrix multiply
r = a @ tx.T  # dont get too caught up by the transpose, the important thing is we're multiplying the array factor by the tx signal
print(r.shape) # 3x10000.  r is now going to be a 2D array, 1D is time and 1D is the spatial dimension

n = np.random.randn(Nr, N) + 1j*np.random.randn(Nr, N)
r = r + 0.1*n # r and n are both 3x10000

plt.plot(np.asarray(r[0,:]).squeeze().real[0:200]) # the asarray and squeeze are just annoyances we have to do because we came from a matrix
plt.plot(np.asarray(r[1,:]).squeeze().real[0:200])
plt.plot(np.asarray(r[2,:]).squeeze().real[0:200])
#plt.plot(np.asarray(r[3,:]).squeeze().real[0:200])
plt.grid()
plt.show()

################################################
# FIND DOA CLASSICAL BEAMFORMER
################################################

theta_scan = np.linspace(-1*np.pi, np.pi, 1000) # 1000 different thetas between -180 and +180 degrees
results = []
for theta_i in theta_scan:
    #print(theta_i)
    w = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta_i)) # look familiar?
    r_weighted = np.conj(w) @ r # apply our weights corresponding to the direction theta_i. remember r is 3x10000 so we can leave w as a normal (row) vector
    results.append(np.mean(np.abs(r_weighted)**2)) # energy detector

# print angle that gave us the max value
print(theta_scan[np.argmax(results)] * 180 / np.pi) # 19.99999999999998

plt.plot(theta_scan*180/np.pi, results) # lets plot angle in degrees
plt.xlabel("Theta [Degrees]")
plt.ylabel("DOA Metric")
plt.grid()
plt.show()

################################################
# FIND DOA CLASSICAL BEAMFORMER POLAR PROJECTION
################################################

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta_scan, results) # MAKE SURE TO USE RADIAN FOR POLAR
ax.set_theta_zero_location('N') # make 0 degrees point up
ax.set_theta_direction(-1) # increase clockwise
ax.set_rgrids([0,2,4,6,8])
ax.set_rlabel_position(22.5)  # Move grid labels away from other labels
plt.show()

################################################
# SWEEPING ANGLE OF ATTACK AFFECT ON SIGNAL
################################################
if False:
    theta_txs = np.concatenate((np.repeat(-90, 10), np.arange(-90, 90, 2), np.repeat(90, 10)))

    theta_scan = np.linspace(-1*np.pi, np.pi, 300)
    results = np.zeros((len(theta_txs), len(theta_scan)))
    for t_i in range(len(theta_txs)):
        #print(t_i)

        theta = theta_txs[t_i] / 180 * np.pi
        a = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta))
        a = a.reshape(-1,1) # 3x1
        tone = np.exp(2j*np.pi*0.02e6*t)
        tone = tone.reshape(-1,1) # 10000x1
        r = a @ tone.T

        for theta_i in range(len(theta_scan)):
            w = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta_scan[theta_i]))
            r_weighted = np.conj(w) @ r # apply our weights corresponding to the direction theta_i
            results[t_i, theta_i]  = np.mean(np.abs(r_weighted)**2) # energy detector

    fig, ax = plt.subplots(1, 1, figsize=(10, 5), subplot_kw={'projection': 'polar'})
    fig.set_tight_layout(True)
    line, = ax.plot(theta_scan, results[0,:])
    ax.set_theta_zero_location('N') # make 0 degrees point up
    ax.set_theta_direction(-1) # increase clockwise
    ax.set_rlabel_position(22.5)  # Move grid labels away from other labels
    text = ax.text(0.4, 12, 'fillmein', fontsize=16)
    text2 = ax.text(np.pi/-2, 19, 'broadside →', fontsize=16)
    text3 = ax.text(np.pi/2, 12, '← broadside', fontsize=16)
    def update(i):
        i = int(i)
        #print(i)
        results_i = results[i,:] / np.max(results[i,:]) * 9 # had to add this in for the last animation because it got too large
        line.set_ydata(results_i)
        d_str = str(np.round(theta_txs[i],2))
        text.set_text('AoA = ' + d_str + '°')
        return line, ax
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(theta_txs)), interval=100)
    anim.save('sweep.gif', writer=PillowWriter(fps=10))
    

################################################
# Capon Beamformer
################################################
if True:
    theta_scan1 = np.linspace(-1*np.pi, np.pi, 1000) # between -180 and +180 degrees
    results1 = []
    for theta_i in theta_scan1:
        a = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta_i))
        a = a.reshape(-1,1) # 3x1

        # Calc covariance matrix
        R = r @ r.conj().T # gives a Nr x Nr covariance matrix of the samples

        Rinv = np.linalg.pinv(R) # 3x3. pseudo-inverse tends to work better than a true inverse

        w = 1/(a.conj().T @ Rinv @ a) # Capon's method! denominator is 1x3 * 3x3 * 3x1
        metric = w[0,0] # convert the 1x1 matrix to a Python scalar, it's still complex though
        metric = np.abs(metric) # take magnitude
        metric = 10*np.log10(metric) # convert to dB so its easier to see small and large lobes at the same time
        results1.append(metric)

    results1 /= np.max(results1) # normalize

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta_scan1, results1) # MAKE SURE TO USE RADIAN FOR POLAR
    ax.set_theta_zero_location('N') # make 0 degrees point up
    ax.set_theta_direction(-1) # increase clockwise
    #ax.set_rgrids([0,2,4,6,8])
    ax.set_rlabel_position(30)  # Move grid labels away from other labels
    plt.show()

################################################
# MUSIC ALGORITHM
################################################
    
if True:
    Nr = 8 # 3 elements
    theta1 = 20 / 180 * np.pi # convert to radians
    theta2 = 25 / 180 * np.pi
    theta3 = -40 / 180 * np.pi
    a1 = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta1))
    a1 = a1.reshape(-1,1)
    a2 = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta2))
    a2 = a2.reshape(-1,1)
    a3 = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta3))
    a3 = a3.reshape(-1,1)
    # we'll use 3 different frequencies
    tone1 = np.exp(2j*np.pi*0.01e6*t)
    tone1 = tone1.reshape(-1,1)
    tone2 = np.exp(2j*np.pi*0.02e6*t)
    tone2 = tone2.reshape(-1,1)
    tone3 = np.exp(2j*np.pi*0.03e6*t)
    tone3 = tone3.reshape(-1,1)
    r = a1 @ tone1.T + a2 @ tone2.T + 0.1 * a3 @ tone3.T
    n = np.random.randn(Nr, N) + 1j*np.random.randn(Nr, N)
    r = r + 0.04*n


    num_expected_signals = 3 # Try changing this!

    # part that doesn't change with theta_i
    R = r @ r.conj().T # Calc covariance matrix, it's Nr x Nr
    w, v = np.linalg.eig(R) # eigenvalue decomposition, v[:,i] is the eigenvector corresponding to the eigenvalue w[i]
    eig_val_order = np.argsort(np.abs(w)) # find order of magnitude of eigenvalues
    v = v[:, eig_val_order] # sort eigenvectors using this order
    # We make a new eigenvector matrix representing the "noise subspace", it's just the rest of the eigenvalues
    V = np.zeros((Nr, Nr - num_expected_signals), dtype=np.complex64)
    for i in range(Nr - num_expected_signals):
        V[:, i] = v[:, i]

    theta_scan = np.linspace(-1*np.pi, np.pi, 1000) # -180 to +180 degrees
    results = []
    for theta_i in theta_scan:
        a = np.exp(-2j * np.pi * d * np.arange(Nr) * np.sin(theta_i)) # array factor
        a = a.reshape(-1,1)
        metric = 1 / (a.conj().T @ V @ V.conj().T @ a) # The main MUSIC equation
        metric = np.abs(metric[0,0]) # take magnitude
        metric = 10*np.log10(metric) # convert to dB
        results.append(metric)

    results /= np.max(results) # normalize

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta_scan, results) # MAKE SURE TO USE RADIAN FOR POLAR
    ax.set_theta_zero_location('N') # make 0 degrees point up
    ax.set_theta_direction(-1) # increase clockwise
    #ax.set_rgrids([0,2,4,6,8])
    ax.set_rlabel_position(30)  # Move grid labels away from other labels
    plt.show()

