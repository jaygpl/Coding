#-----------------------------------------------------------------
# Program Name: Set Operations
# Purpose: The purpose of this program is to allow the user to combine and compare sets using set operations.
# Creator: Jayden
# Student #: 754789
# Date: Apr. 7, 2025
#-----------------------------------------------------------------
# This will define the sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# This will preform the set operations
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

# This will print the results
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)