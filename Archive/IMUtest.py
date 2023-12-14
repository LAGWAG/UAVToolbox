from imusim.all import *

sim = Simulation()
trajectory = RandomTrajectory()
imu = IdealIMU(sim, trajectory)

samplingPeriod = 0.01
behaviour = BasicIMUBehaviour(imu, samplingPeriod)

sim.time = trajectory.startTime

sim.run(trajectory.endTime)