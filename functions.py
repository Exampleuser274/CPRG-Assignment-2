def show_menu():
    '''The main menu
    Returns either 1, 2, 3, or 4 depending on user input'''
    check = True
    print("Welcome to the students record program")
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    while check:

        answer = input("")
        if answer == "1" or answer == "2" or answer == "3" or answer == "4":
            check = False
            continue
        else:
            print("Please enter a valid response")
    return(int(answer))
def add_student(students,id,name,gpa,semester):
    '''
    takes the list of students and the information of a new student and returns an appended list
    the add_function contains this
    '''

    newstudent = { "id":id,"name":name,"gpa":gpa,"semester":semester}
    '''students[id] = [name,gpa,semester]'''
    students.append(newstudent)
    print("Student added")
    for item in students[id]:
        print(item,end=" ")
def remove(students,id):
    '''
    Takes the list of students and the id of a student, then returns the list with the student removed
    the remove_menu function contains this
    '''
    
    for student in students:
        if id == student["id"]:
            students.pop(students.index(student))
            print("Student removed")
    return students
def edit_name(students,id,new):
    '''
    takes the list of students, the id of a student, and the new name for the student, then returns the updated list
    the edit_menu function contains this
    '''
    for student in students:
        if id == student["id"]:
            student["name"] = new
            print("Student name modified for the student with id", id)
            print("Student's new name is",new)
    return(students)
def search(students,id):
    '''
    Checks the id key value for each dictionary in the list then returns the index of the matching id, or -1 if none match
    the search_menu function contains this
    '''
    index = -1
    for student in students:
        if id == student["id"]:
            index = students.index(student)
    return index
def run_search(students):
    '''Menu for the search function'''
    answer = 0
    while answer != -1:
        print("Enter the id of the student. Enter -1 to return to the previous menu")
        answer = int(input(""))
        if answer != -1:
            index = search(students,answer)
            if index == -1:
                print("Student not found")
            else:
                print("Student found")
                print(students[index]["id"],students[index]["name"],students[index]["gpa"],students[index]["semester"])
    
def run_edit(students):
    '''menu for editing stuent name'''
    check = 0
    while check != -1:
        print("Enter the id of the student. Enter -1 to return to the previous menu")
        check = int(input(""))
        if check != -1:
            print("enter new name")
            newname = input("")
            students = edit_name(students,check,newname)
    
def run_add(students):
    '''menu for adding a student'''
    check = True
    while check:
        print("Enter id of the student, followed by the student's information.")
        print("id:")
        student_id = int(input(""))
        print("Name:")
        student_name = input("")
        print("GPA:")
        student_gpa = float(input(""))
        print("Semester:")
        student_semester = input("")
        students = add_student(students,student_id,student_name,student_gpa,student_semester)
        check2 = True
        while check2:
            print("Do you want to add a new student?y(yes)/n(no)")
            check3 = input("").lower
            if check3 == "y" or check3 == "yes":
                check2 = False
            elif check3 == "n" or check3 == "no":
                check2 = False
                check = False
def run_remove(students):
    '''menu for removing a student'''
    check = True
    while check:
        print("Enter id of the student that you want to remove from the students' registry.")
        student_id = int(input(""))
        students = remove(students,student_id)
        check2 = True
        while check2:
            print("Do you want to remove more students?y(yes)/n(no)")
            check3 = input("").lower
            if check3 == "y" or check3 == "yes":
                check2 = False
            elif check3 == "n" or check3 == "no":
                check2 = False
                check = False