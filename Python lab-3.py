
# Assignment - 1/ Lab -3
#==========================

# 1. WAP to reverse aa number using a while loop.

num = int(input("Enter a number: "))
while num != 0:
    remainder = num % 10
    print(remainder, end="")
    num = num // 10
    

        

# 2. WAP to check whether a number is palindrome or not.

num = int(input("Enter a number: "))
rev_num = 0
while num != 0:
    remainder = num % 10
    rev_num = (rev_num * 10) + remainder
    num = num // 10
    if rev_num == num:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
        
        
# 3. WAP finding a factorial of a given number using a while loop.

num = int(input("Enter a number: "))
factorial = 1
while num != 0:
    factorial = factorial * num
    num = num - 1
    print("Factorial of the number is: ", factorial)

# 4. Accept number using input() function until ths user enter . If user input 0 then break the while loop and
#    display thw sum of all the numbers.

num = 0
while num != 0:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    print("Sum of all the numbers is: ", sum)




# Assignment - 2/ Lab -3
#==========================

# 1. Print the first 10 natural number using for loop.

for i in range(1, 11):
    print(i)
    

# 2.  WAP to check if the given string is a palindrome.

s = input("Enter a string: ")
s = s.lower()
rev_s = s[::-1]
if s == rev_s:
    print("String is palindrome")
else:
    print("String is not palindrome")
    

# 3. WAP to check if a given number is an armstrong number.

num = int(input("Enter a number: "))    
sum = 0
for i in range(len(str(num))):
    sum = sum + (int(str(num)[i]))**3
    if sum == num:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")
        

# 4. WAP to get the fibonacci series between 0 to 50.

a, b = 0, 1

print("Fibonacci series between 0 and 50:")
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b


# 5. WAP to check the validity of password input by users?

# Function to check password validity
def is_valid_password(password):
    
    # Initialize flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special_char = False

    # Check length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    # Check for required characters
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special_char = True

    # Check if all conditions are satisfied
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one digit.")
    if not has_special_char:
        print("Password must contain at least one special character from [$#@].")

    # Return True if all conditions are satisfied
    return has_upper and has_lower and has_digit and has_special_char

# Input password from the user
password = input("Enter a password: ")

# Validate the password
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
