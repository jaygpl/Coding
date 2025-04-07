#-----------------------------------------------------------------
# Program Name: Tuple Operations & Count
# Purpose: The purpose of this program is for the user to create a tuple with repeated values.
# Creator: Jayden
# Student #: 754789
# Date: Apr. 2, 2025
#-----------------------------------------------------------------
# This will create a tuple with repeated values
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")

# This will ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")

# This will count occurrences and print the results 
count = fruits.count(fruit_name)
print(f"'{fruit_name}' appears {count} times in the tuple.")
