#---------------------------------------------------------------------------------
# Program Name: Even or Odd Number Checker
# Purpose: This program allows the user to type in a number and uses the data to determine if the numbe that is typed in is either even or odd.
# Creator: Jayden Gopaul
# Student #: 754789
# Date: Mar. 3, 2025
#---------------------------------------------------------------------------------
# This part of the code will ask the user to enter a number
num = int(input("Enter a number: "))

# This part uses a conditional statement to check if the number entered by the user is even or odd.
if num % 2 == 0:
    print("The number is even.") # This will print is the result is even.
else:
    print("The number is odd.") # This will print if the result is odd.