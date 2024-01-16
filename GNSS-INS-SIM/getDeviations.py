import os
import glob
import math
import numpy as np
import csv
import matplotlib.pyplot as plt

from demo_straightLine import *

def getDeviations():
    # Run the IMU SIM
    test_free_integration()

    # Specify the path to the parent directory
    parent_directory = 'demo_saved_data'

    # List all subdirectories in the parent directory
    subdirectories = [d for d in glob.glob(os.path.join(parent_directory, '*')) if os.path.isdir(d)]

    # Sort subdirectories by creation time (most recent first)
    subdirectories.sort(key=lambda x: os.path.getctime(x), reverse=True)

    # Check if there are any subdirectories
    if subdirectories:
        # Get the path of the most recently created subdirectory
        most_recent_subdirectory = subdirectories[0]

        # Change the working directory to the most recently created subdirectory
        #os.chdir(most_recent_subdirectory)

        #print(f"Changed directory to: {most_recent_subdirectory}")
    else:
        #print("No subdirectories found.")
        pass

    # DIRECTORY CHANGE
    os.chdir(most_recent_subdirectory)

    #data_array = np.genfromtxt('time.csv', delimiter=',')
    #print(data_array[2])


    # Specify the paths to your CSV files
    csv_file_path1 = 'pos_algo0_0_LLA.csv'
    csv_file_path2 = 'ref_pos_LLA.csv'

    # Lists to store data from CSV columns
    column1_data1, column2_data1 = [], []
    column1_data2, column2_data2 = [], []

    # Read data from the first CSV file
    with open(csv_file_path1, 'r') as csv_file1:
        csv_reader1 = csv.reader(csv_file1)
        next(csv_reader1)  # Skip the header if present
        for row in csv_reader1:
            column1_data1.append(float(row[0]))
            column2_data1.append(float(row[1]))

    # Read data from the second CSV file
    with open(csv_file_path2, 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)
        next(csv_reader2)  # Skip the header if present
        for row in csv_reader2:
            column1_data2.append(float(row[0]))
            column2_data2.append(float(row[1]))
    
    truePosition=column2_data1,column1_data1
    plannedPosition=column2_data2,column1_data2

    return truePosition, plannedPosition

# Function to collate all the data returned from the function getDeviations above
def collateData(numberDrones):
    coordinates=[]
    for i in range(numberDrones):
        truepos, plannedpos=getDeviations()
        if (i < 1):
            coordinates.append(truepos)
            coordinates.append(plannedpos)
        else:
            coordinates.append(plannedpos)
        
    arr=np.array(coordinates)
    print(arr.shape)
    
collateData(4)
