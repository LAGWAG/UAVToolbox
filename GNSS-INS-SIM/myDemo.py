# -*- coding: utf-8 -*-
# Filename: demo_allan.py

"""
Test Sim with Allan analysis.
Created on 2018-01-23
@author: dongxiaoguang
"""

import os
import math
import numpy as np
from gnss_ins_sim.sim import imu_model
from gnss_ins_sim.sim import ins_sim

# globals
D2R = math.pi/180

motion_def_path = os.path.abspath('.//demo_motion_def_files//')
fs = 100.0          # IMU sample frequency

def test_allan():
    '''
    An Allan analysis demo for Sim.
    '''
    imu_err='mid-accuracy'
    imu = imu_model.IMU(accuracy=imu_err, axis=6, gps=False)

    # do not generate GPS and magnetometer data
    imu = imu_model.IMU(accuracy=imu_err, axis=6, gps=False)

    fs = 100.0

    #### Allan analysis algorithm
    from demo_algorithms import allan_analysis
    algo = allan_analysis.Allan()

    #### start simulation
    sim = ins_sim.Sim([fs, 0.0, 0.0], motion_def_path+"//motion_def-Allan.csv", ref_frame=1,
                      imu=imu,
                      mode=None,
                      env=None,
                      algorithm=algo)
    sim.run()
    # generate simulation results, summary, and save data to files
    sim.results()  # save data files
    # plot data
    sim.plot(['ad_accel', 'ad_gyro'])

if __name__ == '__main__':
    test_allan()
