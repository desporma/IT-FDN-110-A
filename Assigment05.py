# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DEsporma,11.15.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Read ToDoList.txt
file = open(objFile, "r")
for row in file:
    # Break ToDoList.txt into separate rows
    strData = row.split(",")
    # Make elements of each row into elements of dictionary
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
    # Append table with dictionary
    lstTable.append(dicRow)
# Close ToDoList.txt
file.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # Print headers
        print("Current Contents:")
        print("Task", "Priority", sep=" | ")
        # Print data from table
        for row in lstTable:
            print(row["Task"],row["Priority"],sep=" | ")
        # Repeat menu ask
        print("\nWhich option would you like to perform?")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Query user
        usertask = input("Please enter a task: ")
        userpriority = input("Please enter a priority: ")
        # Add user responses to dictionary
        dicRow = {"Task" : usertask, "Priority" : userpriority}
        # Append dictionary to table
        lstTable.append(dicRow)
        # Confirmation and menu ask
        print("\nItem added to list. Which option would you like to perform?")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # Enclose in try-except construct if cannot remove more items
        try:
            # Delete last row from table
            lstTable.remove(dicRow)
            # Confirmation and menu ask.
            print("Most recent task and priority removed from list. Which option would you like to perform?")
        except:
            print("Last new item already removed. Cannot remove further. Please select another option from te menu.")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # Open file
        file = open(objFile, "w")
        # Add rows of table to ToDoList.txt.
        for row in lstTable:
            file.write(row["Task"] + "," + row["Priority"] + "\n")
        file.close()
        # Confirmation and menu ask.
        print("Tasks saved to list. Which option would you like to perform?")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # Say goodbye to user
        print("Successfully exited program.")
        break  # and Exit the program
