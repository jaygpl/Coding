#--------------------------------------------------------------------------------
# Program Name: Skipping Even Numbers
# Purpose: This program will print numbers from 1-10, but will also skip even numbers.
# Creator: Jayden
# Student #: 754789
# Date: Mar. 18, 2025
#--------------------------------------------------------------------------------
# This for loop will generate numbers from 1 to 10
for num in range(1, 11):
    # This checks if the number is even
    if num % 2 == 0:
        continue  # This will skip even numbers and go to the next one

    # This prints the odd number.
    print(num)