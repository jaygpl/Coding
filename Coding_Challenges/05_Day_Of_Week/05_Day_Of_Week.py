#---------------------------------------------------------------------------------
# Program Name: Day of the Week Activity Recommender
# Purpose: This program will tell the user what activity they should do based on the day of week it is.
# Creator: Jayden Gopaul
# Student #: 754789
# Date: Mar. 4, 2025
#--------------------------------------------------------------------------------
# This program will be a day of the week activity reminder that will tell the user what activity they should do based on the day of the week of course.

# The input variable will show the text written in quote and allow the user to enter the day of the week.
day = input("Enter the day of the week: ")

# The if and else statement will show the user one of the quoted text below based on the day entered.
if day == "monday":
    print("Start your week with a workout!")
# An elif works similar to the if and else statement and will also display the text quoted based on the day entered.
elif day == "tuesday":
    print("It's a great day to read a book!")
elif day == "wednesday":
    print("Mid-week movie night!")
elif day == "thursday":
    print("Try a new recipe!")
elif day == "friday":
    print("Relax and enjoy the weekend!")
elif day == "saturday":
    print("Go for a hike!")
elif day == "sunday":
    print("Prepare for the week ahead with some self-care.")
else:
    print("That doesn't seem like a valid day. Please enter a correct day of the week.")