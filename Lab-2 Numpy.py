 
 # Lab-2 NumPy 
 #============
 
# 1. How to find the mean of every NumPy array in the given list.

'''input:
list=[
    np.array([3,2,8,9])
    np.array([4,12,34,25,78])
    np.array([23,12,67])
]'''

import numpy as np

# Input list of numpy arrays
array_list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

# Calculate and print the mean of each array
for i, arr in enumerate(array_list):
    mean_value = np.mean(arr)
    print(f"Mean of array {i+1}: {mean_value}")


# 2. Compute the median of the flattened NumPy array.

# Input array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])

# Compute the median of the array
median_value = np.median(x_odd)
print("Median of the array:", median_value)



# 3. Compute the standard deviation of the NumPy array

# Input array
arr = np.array([20, 2, 7, 1, 34])

# Compute the standard deviation of the array
std_dev = np.std(arr)
print("Standard Deviation of the array:", std_dev)
