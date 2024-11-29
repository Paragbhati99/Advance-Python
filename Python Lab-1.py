
# Using input() function take one number from the user and using ternary operators Check whether the number is even or odd?

num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")
    

#======================================================================

# Using input function take two number an then swap the number?

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1, num2 = num2, num1

print("Swapped numbers are:")
print("Number 1:", num1)
print("Number 2:", num2)

#=======================================================================

# Write a program to convert kilometers to mile in python.
# 1 kilometer = 0.621371 miles

conversion_factor = 0.621371
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * conversion_factor

print(f"{kilometers} kilometers is equal to {miles:.2f} miles")

#========================================================================

# Find the simple interest on Rs.200 for 5 years at 5% per year.
# Simple Interest = (Principal * Rate * Time) / 100

# Given values
P = 200  # Principal amount in Rs
R = 5    # Rate of interest per year
T = 5    # Time in years

# Simple Interest formula
SI = (P * R * T) / 100

print(f"The simple interest is Rs. {SI}")
