import csv
import matplotlib.pyplot as plt

# Specify the path to your CSV file
csv_file_path = 'pos_algo0_0.csv'

# Lists to store data from CSV columns
column1_data = []
column2_data = []

# Read data from CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header if present
    for row in csv_reader:
        # Assuming the first two columns contain numeric data
        column1_data.append(float(row[0]))
        column2_data.append(float(row[1]))

# Plotting the data
plt.plot(column1_data, column2_data, marker='o', linestyle='-', color='b')
plt.title('Plot of First Two Columns from CSV')
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.grid(True)
plt.show()
