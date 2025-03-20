#--------------------------------------------------------------------------------
# Program Name: Skipping Even Numbers
# Purpose: This program will be used to write a number that starts at `10` and counts down to `1`, but if the user enters `"stop"`, the countdown should break.
# Creator: Jayden
# Student #: 754789
# Date: Mar. 18, 2025
#--------------------------------------------------------------------------------
# This loop is used to display the countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)  # This print command will show the current countdown number

    # This input will ask the user to stop or continue
    user_input = input('Enter "stop" to cancel or press Enter: ')

    # If the user types "stop", it will break the loop
    if user_input.lower() == "stop":
        print("Countdown stopped!")
        break