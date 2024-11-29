
# WAP to check leap year in python?

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
            
#==============================================================

# WAP find a largest among three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
    
    
#==================================================================================

# WAP to check if a number is positive , Negative or 0?

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#==================================================================================

'''4. A toy vendor supplies three types of toys: Battery Based Toys,
 Key-based Toys, and Electrical Charging Based Toys. 
 The vendor gives a discount of 10% on orders for battery-based toys 
 if the order is for more than Rs. 1000. On orders of more than 
 Rs. 100 for key-based toys, a discount of 5% is given, 
 and a discount of 10% is given on orders for electrical charging based toys of
 value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys,
 key-based toys, and electrical charging based toys respectively. 
 Write a program that reads the product code and the order amount and prints out the net amount 
 that the customer is required to pay after the discount.'''

# Input from the user
product_code = int(input("Enter product code (1 for Battery-Based, 2 for Key-Based, 3 for Electrical Charging-Based): "))
order_amount = float(input("Enter the order amount: "))

discount = 0

if product_code == 1:  # Battery-Based Toys
    if order_amount > 1000:
        discount = 0.10  # 10% discount
elif product_code == 2:  # Key-Based Toys
    if order_amount > 100:
        discount = 0.05  # 5% discount
elif product_code == 3:  # Electrical Charging-Based Toys
    if order_amount > 500:
        discount = 0.10  # 10% discount
else:
    print("Invalid product code.")

net_amount = order_amount - (order_amount * discount)

print(f"The net amount to be paid is: Rs. {net_amount:.2f}")


#=============================================================================================================================


#5. A transport company charges the fare according to following table:

'''
Distance      Charges 
1-50          8 Rs./Km
51-100        10 Rs./Km
> 100         12 Rs/Km
'''

distance = float(input("Enter the distance traveled (in Km): "))

# Calculate the fare based on the distance
if 1 <= distance <= 50:
    fare = distance * 8  # Rs. 8 per Km
elif 51 <= distance <= 100:
    fare = distance * 10  # Rs. 10 per Km
elif distance > 100:
    fare = distance * 12  # Rs. 12 per Km
else:
    fare = 0
    print("Invalid distance entered!")

# Display the total fare
if fare > 0:
    print(f"The total fare is: Rs. {fare:.2f}")
