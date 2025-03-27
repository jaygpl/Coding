#-----------------------------------------------------------------
# Program Name: Create a Grocery List and Add Items
# Purpose: The purpose of this program is that it will create a grocery list for the user to add cheese and tomatoes to it.
# Creator: Jayden
# Student #: 754789
# Date: mar. 21, 2025
#-----------------------------------------------------------------
# This will be the initial grocery list
grocery_list = ['apples', 'bread', 'milk', 'eggs']

# This will ask the user if they want to add cheese to the grocery list
add_cheese = input('Do you want to add cheese to the list? (yes/no): ').lower()
if add_cheese == 'yes':
    grocery_list.append('cheese')

# This will ask the user if they want to add tomatoes to the grocery list
add_tomatoes = input('Do you want to add tomatoes to the list? (yes/no): ').lower()
if add_tomatoes == 'yes':
    grocery_list.append('tomatoes')

# This will update the grocery list with the new items added
print('Updated grocery list:', grocery_list)






