''''
Student Records Program
_______________________

This program provides an interactive, menu-driven interface for managing
a collection of student records. Each student is stored in a dictionary
using their unique ID as the key. The program allows users to:

    • Search for a student by ID
    • Edit an existing student's information
    • Add new students to the registry
    • Remove students from the registry

The "functions" module contains all processing logic such as adding,
searching, editing, and removing student entries, while this file (main file)
handles the main program loop and user interaction.

Data Structure:
    students = {
        student_id : {
            "name"     : string,
            "id"       : string,
            "gpa"      : float,
            "semester" : string
        }
    }

Program Flow:
    1. Display menu options to the user.
    2. Execute the selected operation.
    3. Ask whether the user wants to continue or exit.
    4. Loop until the user chooses to quit.

Authors: (Alexander Kovach, Ryan Dezall)

'''



import functions as fn

students = {}

while True:
    option = fn.show_menu()

    if option == 1:
        fn.run_search(students)
    elif option == 2:
        fn.run_edit(students)
    elif option == 3:
        fn.run_add(students)
    elif option == 4:
        fn.run_remove(students)
    
    print("Would you like to continue(y/yes), or exit the program(n/no)")
    choice = input("").lower()
    if choice == "yes" or choice == "y":
        continue
    if choice == "no" or choice == "n":
        break
    else:
        print("Please enter a valid response")
