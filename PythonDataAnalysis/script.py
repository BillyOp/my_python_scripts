import csv
import numpy as np
# or import numpy
# or from numpy import math

# Opening a CSV with python language
with open("winequality-red.csv", 'r') as f:
    wines = list(csv.reader(f, delimiter=";"))
print(wines[:3])

#Convert the wine list into a numpyarray
wine_list_narray = np.array(wines[1:], dtype=np.float)
print(wine_list_narray)
print(wine_list_narray.shape)
print(wine_list_narray[:,-1])
average = np.average(wine_list_narray[:,-1])
print(average)
#convert everything to float



# Find the average quality of the wines
# Create a list of quality_column
list_of_wines = wines[1:][-1]
print(list_of_wines)

#List comprehension in python
qualities = [float(item[-1]) for item in wines[1:]]
print(qualities)
average = sum(qualities)/len(qualities)
print(average)

#Creating and empty numpy array
no_of_rows = 1
no_of_columns = 2
empty_numpy = np.zeros((no_of_rows, no_of_columns))
print(empty_numpy)


#Numpy array with random_values
random_value_numpy = np.random.rand(no_of_rows, no_of_columns)
print(random_value_numpy)

# Numpy get form text function to read data into csv files
# function genfromtxt
wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)
print(wines)

# Accessing a numpy details
# wines[,] ---- wines[row_details, column_details]

# Slicing numpy arrays [:]
# N-dimensional numpy arrays

# Converting and ndarray into a different type
wines.astype(int)
wines.astype(np.int32) # When one has memory concerns
