#  In this task, we'll create a program that allows a teacher to keep track of the grades for their students.
#  The program will store and manipulate the data
def start():
    operations = {
        1: "Add new student",
        2: "Add assignment",
        3: "Add grade",
        4: "Average grade",
        5: "student report",
        6: "class report",
        7: "quit"
    }
    print("_________________ operation list __________________________")
    for operation in operations.items():
        print(f'{operation[0]}) {operation[1]}')
#     validation for operation input
    try:
        operation_number = int(input("Select operation number from the list: "))
        if operation_number < 1 or operation_number > 7:
            print("Invalid input: please select a number from the list")
        elif operation_number == 1:
            student_name = input("Enter student name: ")
            add_new_student(student_name)
            print(grade_book)
    except ValueError:
        print("please enter a number from the list ex: 1")
        start()


# methods for the program
# adding a new student
def add_new_student (name):
    # validation for the student name
    student_name_errors = []
    if len(name) < 3:
        student_name_errors.append("student name must be at least 3 characters")
    if name.isnumeric():
        student_name_errors.append("student name must be letters")
    if any(c in "!@#$%^&*()~{}[]';:?><)," for c in name):
        student_name_errors.append("student name must be only characters")
    while len(student_name_errors) >0:
        for error in student_name_errors:
            print(error)
            start()
        break
    else:
        grade_book[name] = {}

# method to add assignment
def add_assignment(assignment):
    for student in grade_book:
        grade_book[student][assignment] = None



if __name__ == '__main__':
    grade_book = {}
    start()
