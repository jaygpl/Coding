#-----------------------------------------------------------------
# Program Name: List Comprehensions and Filtering
# Purpose: The purpose of this program will allow the user to use list comprehensions to filter and manipulate data based on a condition.
# Creator: Jayden
# Student #: 754789
# Date: mar. 25, 2025
#-----------------------------------------------------------------
# This will be the initial list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# This will use a list comprehension to take out the odd numbers and leave even ones
even_numbers = [num for num in numbers if num % 2 == 0]

# This will use the comprehension to get squares pf even numbers
squared_numbers = [num ** 2 for num in even_numbers]

# This will print the results
print("even_numbers =", even_numbers)
print("squared_numbers =", squared_numbers)