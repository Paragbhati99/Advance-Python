 #Lab-1 Numpy Situation Question
 
 
# 1. Hi I am new to Python numpy. Can you generate some real world situations where I can use a numpy array with some source code.

import numpy as np

# Sample temperature data in Celsius for 30 days
temperatures = np.array([30.5, 32.1, 29.8, 31.0, 33.5, 35.0, 34.2, 32.5, 31.8, 33.0, 
                         30.0, 29.5, 28.7, 31.2, 32.8, 33.4, 34.0, 35.5, 34.1, 33.7, 
                         30.2, 29.9, 31.3, 32.7, 33.9, 34.3, 30.8, 29.7, 28.9, 30.4])

# Calculate average, max, and min temperatures
average_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

print("Average Temperature:", average_temp)
print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)


# 2. Hi! Let's create a real-life example involving weather data. Use NumPy to analyze temperature data for a week, 
# perform slicing, indexing, shaping, and reshaping operations, and calculate various statistics.

import numpy as np

# Generate sample hourly temperature data for 7 days
temperature_data = np.array([
    [12, 14, 13, 15, 17, 20, 22, 25, 27, 30, 32, 33, 31, 29, 27, 25, 23, 22, 21, 20, 18, 17, 16, 14],
    [11, 13, 12, 14, 16, 19, 21, 24, 26, 29, 31, 32, 30, 28, 26, 24, 22, 21, 20, 19, 17, 16, 15, 13],
    [10, 12, 11, 13, 15, 18, 20, 23, 25, 28, 30, 31, 29, 27, 25, 23, 21, 20, 19, 18, 16, 15, 14, 12],
    [9,  11, 10, 12, 14, 17, 19, 22, 24, 27, 29, 30, 28, 26, 24, 22, 20, 19, 18, 17, 15, 14, 13, 11],
    [8,  10, 9,  11, 13, 16, 18, 21, 23, 26, 28, 29, 27, 25, 23, 21, 19, 18, 17, 16, 14, 13, 12, 10],
    [7,   9, 8,  10, 12, 15, 17, 20, 22, 25, 27, 28, 26, 24, 22, 20, 18, 17, 16, 15, 13, 12, 11,  9],
    [6,   8, 7,   9, 11, 14, 16, 19, 21, 24, 26, 27, 25, 23, 21, 19, 17, 16, 15, 14, 12, 11, 10,  8]
])

temp_noon_day3 = temperature_data[2, 11]
print("Temperature at noon on the third day:", temp_noon_day3)

midnight_temps = temperature_data[:, 0]
print("Midnight temperatures for each day:", midnight_temps)

morning_temps_day1 = temperature_data[0, 8:13]
print("Morning temperatures on the first day (8 AM to 12 PM):", morning_temps_day1)

reshaped_data = temperature_data.reshape(168, 1)
print("Reshaped data (168, 1):\n", reshaped_data)

daily_max_temps = np.max(temperature_data, axis=1)
daily_min_temps = np.min(temperature_data, axis=1)

print("Daily maximum temperatures:", daily_max_temps)
print("Daily minimum temperatures:", daily_min_temps)

weekly_avg_temp = np.mean(temperature_data)
print("Weekly average temperature:", weekly_avg_temp)

daily_avg_temps = np.mean(temperature_data, axis=1)
print("Daily average temperatures:", daily_avg_temps)

weekly_max_temp = np.max(temperature_data)
weekly_min_temp = np.min(temperature_data)

print("Weekly maximum temperature:", weekly_max_temp)
print("Weekly minimum temperature:", weekly_min_temp) 


# 2. convert the below into a numpy array then display the array the first and last index 
# and then multiply each element by 2 and display the result. 

# Input list
my_list = [1, 2, 3, 4, 5]

# Step 1: Convert the list into a numpy array
my_array = np.array(my_list)
print("Array:", my_array)

# Step 2: Display the first and last elements
first_element = my_array[0]
last_element = my_array[-1]
print("First Element:", first_element)
print("Last Element:", last_element)

# Step 3: Multiply each element by 2
doubled_array = my_array * 2
print("Doubled Array:", doubled_array)



# Lab-3 Working with Numpy using Jupyter
#=======================================


# 2. write a numpy program to create an array of 10 zeros, 10 ones, and 10 fives. 

'''sample output:
==================
An array of 10 zeros:
[0,0,0,0,0,0,0,0,0,0]

An array of 10 ones:
[1,1,1,1,1,1,1,1,1,1]

An array of 10 fives:
[5,5,5,5,5,5,5,5,5,5]
'''

# Create an array of 10 zeros
zeros_array = np.zeros(10, dtype=int)
print("An array of 10 zeros:")
print(zeros_array)

# Create an array of 10 ones
ones_array = np.ones(10, dtype=int)
print("\nAn array of 10 ones:")
print(ones_array)

# Create an array of 10 fives
fives_array = np.full(10, 5)
print("\nAn array of 10 fives:")
print(fives_array)



# 3. write a Numpy program to create a 3x3 matrix with values ranging from 2 to 10. 

''' Sample output: 

[[2 3 4]
[5 6 7]
[8 9 10]]
'''

# Create a 3x3 matrix with values from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 matrix with values from 2 to 10:")
print(matrix)
