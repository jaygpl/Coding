#-----------------------------------------------------------------
# Program Name: Student Grading System
# Purpose: This program takes the score out of 100 from students, and shows what their grade is for that score.
# Creator: Jayden
# Student #: 754789
# Date: Feb. 25, 2025
#-----------------------------------------------------------------

# This input prompt will tell students to put their score out of 100.
score = float(input("Enter your score (out of 100): "))

# This will be determining the grade for the score that the student provides.
if score >= 90:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")