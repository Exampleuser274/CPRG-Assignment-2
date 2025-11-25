import functions as fn

students = {}

while True:
    option = fn.show_menu()

    if option == 1:
        students = fn.run_search(students)
    elif option == 2:
        students = fn.run_edit(students)
    elif option == 3:
        students = fn.run_add(students)
    elif option == 4:
        students = fn.run_remove(students)
    
    print("Would you like to continue(y/yes), or exit the program(n/no)")
    choice = input("").lower()
    if choice == "yes" or choice == "y":
        continue
    if choice == "no" or choice == "n":
        break
    else:
        print("Please enter a valid response")
