#-----------------------------------------------------------------------------------
# Program Name: Temperature Advice
# Purpose: This program suggests the user on what they should wear, based off the temperature that is around you.
# Creator: Jayden
# Student #: 754789
# Date: Feb. 27, 2025
#-----------------------------------------------------------------------------------

# This step will ask the user to enter the temperature of the weather. (in Celsius)
temperature = float(input("Enter the temperature (in Celsius): "))

# Now this part of the code will tell the user what they should wear based off the temp provided.
# For this code I used the if and else statement, as well as an Elif.
if temperature < 10:
    print("It's cold outside. Wear a jacket!")
elif 10 <= temperature <= 25:
    print("It's a nice day. Wear short-sleeves!")
else:
    print("It's hot outside. Stay cool!")