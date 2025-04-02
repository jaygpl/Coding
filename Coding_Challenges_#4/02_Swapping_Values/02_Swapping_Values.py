#-----------------------------------------------------------------
# Program Name: Swapping Values Using Tuples
# Purpose: The purpose of this program will allow the user to input 2 numbers and store them in a tuple.
# Creator: Jayden
# Student #: 754789
# Date: Apr. 1, 2025
#-----------------------------------------------------------------
# This will ask the user to input 2 numbers into the tuple
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# This will store the numbers in the tuple
values = (num1, num2)

# This will swap the values using tuple unpacking
num1, num2 = num2, num1

# This will print the swapped values
print("Swapped values:", (num1, num2))
