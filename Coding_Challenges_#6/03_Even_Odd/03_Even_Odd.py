#-----------------------------------------------------------------
# Program Name: Check Even or Odd
# Purpose: The purpose of this program is to allow the user to create a function that takes a number and returns true if even or false if it's odd.
# Creator: Jayden
# Student #: 754789
# Date: May. 2, 2025
#-----------------------------------------------------------------
def is_even(number):
    return number % 2 == 0

# this contains the logic to get input from the user and display whether the number is even or odd
def main():
    try:
        num = int(input("Enter a number: "))

        # this will assist in printing out if the number is even or odd
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Please enter a valid integer.")

# this will call the main function to run the program
main()
