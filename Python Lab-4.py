

# Python Lab - 4 Assignment-1
#=============================

# 1. Write a python program to sum all the items in a list.

# Define the list of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum using the built-in sum() function
total = sum(numbers)

# Print the result
print("The sum of all items in the list is:", total)


# 2. Write a python program to get the largest and smallest number from a list without builtin functions.

numbers = [4, 2, 9, 1, 5, 6]

# Initialize variables to store the largest and smallest numbers
# Set the initial values to the first element in the list
largest = numbers[0]
smallest = numbers[0]

# Loop through each number in the list
for num in numbers:
    # Check if the current number is larger than the largest so far
    if num > largest:
        largest = num
    # Check if the current number is smaller than the smallest so far
    if num < smallest:
        smallest = num

# Print the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

        
        
# 3. Write a python program to find the first duplicate a list and display those.

numbers = [3, 5, 2, 3, 7, 5, 8, 9, 2, 10]

duplicates = [] # Initialize an empty list to store duplicates

seen = set()# Initialize an empty set to keep track of seen numbers

# Loop through each number in the list
for num in numbers:
    # Check if the number has already been seen
    if num in seen:# If it's not already in duplicates, add it
        if num not in duplicates:
            duplicates.append(num)
    else: # Add the number to seen set if not seen before
        seen.add(num)

# Display the first duplicate and all duplicates
if duplicates:
    print("The first duplicate is:", duplicates[0])
    print("All duplicates in the list are:", duplicates)
else:
    print("No duplicates found.")

        

# 4. Write a python program to split a given list into two parts where the length of the first part of the list is given.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_part_length = 5

# Split the list into two parts
first_part = numbers[:first_part_length]
second_part = numbers[first_part_length:]

# Print the results
print("First part of the list:", first_part)
print("Second part of the list:", second_part)


# 5. Write a python program to traverse a given list in reverse order and print the elements with the original index.
'''Original List:
['red', 'green', 'white', 'black']

Traverse the said list in reverse order - black white green red'''

# Define the original list
colors = ['red', 'green', 'white', 'black']

# Print the original list
print("Original List:")
print(colors)

# Traverse the list in reverse order and print elements with their original index
print("\nTraverse the said list in reverse order:")
for i in range(len(colors) - 1, -1, -1):
    print(f"{colors[i]} (original index {i})")




# Python Lab - 4 Assignment-2
#=============================


# 1. Write a python program and calculate the mean of the below dictionary

test_dict={"A":6,"B":9,"C":5,"D":7,"E":4}
total_sum = sum(test_dict.values()) # Calculate the sum of all values in the dictionary

count = len(test_dict) # Calculate the number of items in the dictionary

mean = total_sum / count # Calculate the mean

# Print the result
print("The mean of the dictionary values is:", mean)



# 2. Write a python script to concatenate the following dictionaries to create a new one.

'''Sample Dictionary:

dic1={1:10,2:20}
dic2={3:30,4:40}
dic1={5:50,6:60}'''

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating the given dictionaries
combined_dict = {**dic1, **dic2, **dic3}

# Print the result
print("Concatenated Dictionary:", combined_dict)


# 3. Write a python program to get the key, value and item in a dictionary.

# input:dict_num={1:10,2:20,3:30,4:40,5:50,6:60}

# Define the dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Traverse the dictionary and print the key, value, and item (key-value pair)
for key, value in dict_num.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")


# 4. write a python program to get the key, value and item in a dictionary.

dict_num = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

# Traverse the dictionary and print the key, value, and item (key-value pair)
for key, value in dict_num.items():
    # Format the output
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")




# Python Lab - 4 Assignment-3
#=============================


# 1. write a python program to find the number of times 4 appears in the tuple.

x = (2, 4, 5, 6, 2, 3, 4, 4, 7)
count_4 = x.count(4)
print("Number of times 4 appears:", count_4)


# 2. write a python program to convert a list to a tuple.

x = [5, 10, 7, 4, 15, 3]

# Convert list to tuple
x_tuple = tuple(x)

print("Tuple:", x_tuple)


# 3. write a python program to calculate the sum of the numbers in a given tuple.

x = [(1, 2), (3, 4), (5, 6)]

# Calculate the sum of all numbers in the tuples
total_sum = sum(sum(pair) for pair in x)
print("Sum of all numbers:", total_sum)


# 4. write a python program and iterate the given tuples.

# Given employee tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# List of employees
employees = [employee1, employee2, employee3]

# Iterate over each employee tuple and print details
for employee in employees:
    name, emp_id, department, salary = employee
    print(f"Name: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Department: {department}")
    print(f"Salary: {salary}")
    print("-" * 30)



# Python Lab - 4 Assignment- 4
#==============================


# 1. write a python program to get only unique items from two sets.

# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Find unique items (symmetric difference)
unique_items = set1.symmetric_difference(set2)

print("Unique items:", unique_items)


# 2. write a python program to return a set of element present in set A or B, but not both .

# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Elements present in either set1 or set2, but not both (symmetric difference)
result = set1 ^ set2

print("Elements present in set1 or set2, but not both:", result)



# 3. write a python program to check if two sets have any elements in common, if yes, display the common elements.

# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Find common elements using intersection
common_elements = set1.intersection(set2)

# Check if there are any common elements and display them
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements found.")


# 4. write a python program to Remove item from set1 that are not common to both set1 and set2.

# Given sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Update set1 to keep only elements common to both sets
set1.intersection_update(set2)

print("Updated set1 with only common elements:", set1)
