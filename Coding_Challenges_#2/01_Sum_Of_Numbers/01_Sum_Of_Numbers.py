#--------------------------------------------------------------------------------
# Program Name: Sum of Numbers
# Purpose: This program will ask the user for a number 'n' and will calculate the sum of all numbers from '1' to 'n' using a 'for' loop.
# Creator: Jayden Gopaul
# Student #: 754789
# Date: Mar. 4, 2025
#--------------------------------------------------------------------------------
# This will allow the user to enter a number of choice.
n = int(input("Enter a number to find out the sum: "))

# This prompt will initialize sum variable
total_sum = 0

# A 'for' loop is being used to add numbers from 1 to n.
for i in range(1, n + 1):
    total_sum += i

# This will print the result of answer for the user to see.
print("Sum =", total_sum)
