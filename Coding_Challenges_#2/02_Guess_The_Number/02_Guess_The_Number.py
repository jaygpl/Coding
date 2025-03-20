#--------------------------------------------------------------------------------
# Program Name: Sum of Numbers
# Purpose: This program will generate a random number and allow the user to guess the number that the program chose from 1-10.
# Creator: Jayden
# Student #: 754789
# Date: Mar. 7, 2025
#--------------------------------------------------------------------------------
import random

# This code will choose a random number from 1-10.
secret_number = random.randint(1, 10)

# This will allow the user to guess the number that the program chose.
while True:
    guess = int(input("Guess the number from 1-10: "))

# This if statement will let the user know if they picked the right number.
    if guess == secret_number:
        print("Correct! 🎉")
        break
# This else statement will show the user the text quoted below if the number they chose was wrong.
    else:
        print("Wrong, try again!")