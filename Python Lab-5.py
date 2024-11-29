
# Python Lab - 5 Assignment-1
#=============================

# 1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def display_file_content():
    try:
        with open("ABC.txt", "r") as file:
            for line in file:
                print(line, end="")  # Using end="" to avoid double newlines
    except FileNotFoundError:
        print("The file 'ABC.txt' was not found.")

# Call the function
display_file_content()



# 2. Write a function in python to count and display the total number of words in a text file "ABC.txt"

def count_words_in_file():
    try:
        with open("ABC.txt", "r") as file:
            total_words = 0
            for line in file:
                words = line.split()  # Split each line into words
                total_words += len(words)  # Count words in the line and add to total
            print("Total number of words:", total_words)
    except FileNotFoundError:
        print("The file 'ABC.txt' was not found.")

# Call the function
count_words_in_file()



# 3. Write a function in python to count uppercase character in a text file "ABC.txt"

def count_uppercase_characters():
    try:
        with open("ABC.txt", "r") as file:
            uppercase_count = 0
            for line in file:
                for char in line:
                    if char.isupper():  # Check if the character is uppercase
                        uppercase_count += 1
            print("Total number of uppercase characters:", uppercase_count)
    except FileNotFoundError:
        print("The file 'ABC.txt' was not found.")

# Call the function
count_uppercase_characters()


# 4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    """Reads words from 'story.txt' and displays those with less than 4 characters."""
    try:
        with open("story.txt", "r") as file:
            for line in file:
                # Split the line into words
                words = line.split()
                # Display words that are less than 4 characters
                short_words = [word for word in words if len(word) < 4]
                for word in short_words:
                    print(word)
    except FileNotFoundError:
        print("The file 'story.txt' was not found.")

# Call the function
display_words()



# Python Lab - 5 Assignment-2
#=============================



# 1. Write a python program to handle a ZeroDivisionError exception when dividing a number by zero.

def safe_divide():
    try:
        # Prompt the user for the numerator and denominator
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform the division
        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is {result}.")
    
    except ZeroDivisionError:
        print("Error: You cannot divide by zero. Please enter a non-zero denominator.")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Call the function
safe_divide()



# 2. Write a python program that prompt the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def input_integer():
    while True:
        try:
            # Prompt the user for input
            user_input = input("Please enter an integer: ")
            # Attempt to convert the input to an integer
            value = int(user_input)
            print(f"You have entered a valid integer: {value}")
            break  # Exit the loop if the conversion is successful
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

# Call the function
input_integer()


# 3. Write a python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

def open_file(filename):
    try:
        # Try to open the specified file in read mode
        with open(filename, "r") as file:
            content = file.read()  # Read the content of the file
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Specify the filename to be opened
file_name = "example.txt"  # Change this to the name of the file you want to open
open_file(file_name)


# 4. Write a python program that prompt the user to input two number and raises a TypeError exception if the inputs are not numerical.

def get_numbers():
    try:
        # Prompt user for input
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        # Try to convert inputs to float
        num1 = float(num1)
        num2 = float(num2)

        return num1, num2

    except ValueError:
        raise TypeError("Both inputs must be numerical values.")

if __name__ == "__main__":
    try:
        number1, number2 = get_numbers()
        print(f"You entered: {number1} and {number2}")
    except TypeError as e:
        print(e)
