#-----------------------------------------------------------------
# Program Name: Subsets and Supersets
# Purpose: The purpose of this program is to allow the user to work with subsets and supersets to understand how they operate.
# Creator: Jayden
# Student #: 754789
# Date: Apr. 7, 2025
#-----------------------------------------------------------------
# This will define the sets
set_a = {1, 2, 3, 4, 5}
set_b = {2, 3, 4}

# This will check the subset and superset relationships
is_subset = set_b.issubset(set_a)
is_superset = set_a.issuperset(set_b)

# This will print the final results
print(is_subset)
print(is_superset)