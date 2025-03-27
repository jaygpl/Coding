#-----------------------------------------------------------------
# Program Name: Access amd Modify List Items
# Purpose: The purpose of this program is to allow the user to remove an item from a list.
# Creator: Jayden
# Student #: 754789
# Date: mar. 27, 2025
#-----------------------------------------------------------------
# This is the initial list
todo_list = ['write email', 'finish homework', 'call mom', 'clean room']

# This will remove the text "call mom" from the list
todo_list.remove('call mom')

# This will print the updated list with "call mom" removed
print(todo_list)

# This will remove "clean room"
todo_list.remove('clean room')

# This will print the final list with "clean room" being removed as well
print(todo_list)