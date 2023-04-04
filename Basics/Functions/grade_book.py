#  In this task, we'll create a program that allows a teacher to keep track of the grades for their students.
#  The program will store and manipulate the data
import sys


def start():
    operations = {
        1: "Add new student",
        2: "Add assignment",
        3: "Add grade",
        4: "student report",
        5: "class report",
        6: "quit"
    }
    print("_________________ operation list __________________________")
    for operation in operations.items():
        print(f'{operation[0]}) {operation[1]}')
    #     validation for operation input
    try:
        operation_number = int(input("Select operation number from the list: "))
        if operation_number < 1 or operation_number > 6:
            print("Invalid input: please select a number from the list")
        elif operation_number == 1:
            student_name = input("Enter student name: ")
            add_new_student(student_name)
        elif operation_number == 2:
            assignment_name = input("Please enter the name of assignment: ")
            add_assignment(assignment_name)
        elif operation_number == 3:
            student_name = input("Enter student name: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter the grade: ")
            add_grade(grade, student_name, assignment_name)
        elif operation_number == 4:
            student_name = input('Enter the student name: ')
            print_student_report(student_name)
        elif operation_number == 5:
            print_class_report()
        elif operation_number == 6:
            sys.exit("Thanks for using our system ")

    except ValueError:
        print("please enter a number from the list ex: 1")
        start()


# methods for the program
# adding a new student
def add_new_student(name):
    # validation for the student name
    student_name_errors = []
    if len(name) < 3:
        student_name_errors.append("student name must be at least 3 characters")
    if name.isnumeric():
        student_name_errors.append("student name must be letters")
    if any(c in "!@#$%^&*()~{}[]';:?><)," for c in name):
        student_name_errors.append("student name must be only characters")
    if not name.isalpha():
        student_name_errors.append("Assignment must be only letters")
    while len(student_name_errors) > 0:
        for error in student_name_errors:
            print(error)
            start()
        break
    else:
        grade_book[name] = []
        start()


# method to add assignment
def add_assignment(assignment):
    # validation for assignment name:
    assignment_name_errors = []
    if len(assignment) < 3:
        assignment_name_errors.append("student name must be at least 3 characters")
    if assignment.isnumeric():
        assignment_name_errors.append("student name must be letters")
    if any(c in "!@#$%^&*()~{}[]';:?><)," for c in assignment):
        assignment_name_errors.append("student name must be only characters")
    if not assignment.isalpha():
        assignment_name_errors.append("Assignment must be only letters")
    while len(assignment_name_errors) > 0:
        for error in assignment_name_errors:
            print(error)
            start()
        break
    else:
        assignments.append(assignment)
        start()


def add_grade(grade, student_name, assignment_name):
    inputs_error = []
    if student_name not in grade_book.keys():
        inputs_error.append("Student name does not exist")
    if assignment_name not in assignments:
        inputs_error.append("Assignment does not exist")
    if not grade.isnumeric():
        inputs_error.append("Grade must be number from 0-99")

    while len(inputs_error) > 0:
        for error in inputs_error:
            print(error)
            start()
        break
    else:
        grade_book[student_name].append(float(grade))
        start()


def average_grade_for_specific_student(student_name):
    new_grades = []
    for grade in grade_book[student_name]:
        new_grade = float(grade)
        new_grades.append(new_grade)
    average = sum(new_grades) / len(grade_book[student_name])
    return average


def average_students():
    new_student_grades = []
    for student_grades in grade_book.items():
        for student_grade in student_grades[1]:
            new_student_grade = int(student_grade)
            new_student_grades.append(new_student_grade)
        average_grade = sum(new_student_grades) / len(new_student_grades)
    return average_grade


def print_student_report(student_name):
    print(f"{student_name}'s grade: ")
    for ass in assignments:
        print(f"{ass}: {grade_book[student_name]}")
    print(f"Average grades: {average_grade_for_specific_student(student_name)}")
    start()


def print_class_report():
    if len(grade_book) == 0:
        print("Please add new students and assignments")
        start()
    for student in grade_book.keys():
        print(f"{student}'s Grades: ")
        for assi in assignments:
            print(f"{assi}: {grade_book[student]}")
        print(f"Average grades: {average_students()}")
    start()


if __name__ == '__main__':
    grade_book = {}
    assignments = []
    start()
