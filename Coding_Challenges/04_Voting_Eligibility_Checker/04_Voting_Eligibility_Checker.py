#---------------------------------------------------------------------------------
# Program Name: Voting Eligibility Checker
# Purpose: This program will inform the user whether they are eligible or not to vote based on their age.
# Creator: Jayden Gopaul
# Student #: 754789
# Date: Mar. 3, 2025
#--------------------------------------------------------------------------------
# This is a simple code that will tell you if you are eligible to vote or not based on your age.

# This input variable will be used to determine the users age.
age = int(input("Enter your age: "))

# The if and else statement will show one of the text quoted below, depending on whatever age you enter.
if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")