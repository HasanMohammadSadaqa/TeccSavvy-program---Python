"""
student grading system, is a system that aims to calculate the grade of many student in many courses
"""
import abc
from abc import ABC


class Person:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def set_name(self, new_name):
        self.__name = new_name
        return self.__name

    def set_age(self, new_age):
        self.__age = new_age
        return self.__age

    def set_email(self, new_email):
        self.__email = new_email
        return self.__email


class Student(Person):
    def __init__(self, name, age, email, major, student_id):
        super().__init__(name, age, email)
        self.__major = major
        self.__student_id = student_id
        self.__enrolled_courses = []

    def get_major(self):
        return self.__major

    def get_student_id(self):
        return self.__student_id

    def get_enrolled_courses(self):
        return self.__enrolled_courses

    def set_major(self, new_major):
        self.__major = new_major
        return self.__major

    def set_id(self, new_id):
        self.__student_id = new_id
        return self.__student_id

    def enroll_a_course(self, course: object):
        self.__enrolled_courses.append(course)


class Instructor(Person):
    def __init__(self, name, age, email, instructor_id):
        super().__init__(name, age, email)
        self.__instructor_id = instructor_id
        self.__courses_taught = []

    def get_id(self):
        return self.__instructor_id

    def get_taught_courses(self):
        return self.__courses_taught

    def set_id(self, new_id):
        self.__instructor_id = new_id
        return self.__instructor_id

    def add_course(self, course: object):
        self.__courses_taught.append(course)


class Course:
    def __init__(self, name, instructor: object):
        self.__name = name
        self.__instructor = instructor
        self.__students = []
        self.__assignments = {}

    def get_name(self):
        return self.__name

    def get_instructor(self):
        return self.__instructor

    def get_student_enrolled(self):
        return self.__students

    def get_assignments(self):
        return self.__assignments

    def set_name(self, new_name):
        self.__name = new_name
        return self.__name

    def set_instructor(self, instructor: object):
        self.__instructor = instructor

    def add_student(self, student: object):
        self.__students.append(student)

    def add_assessment(self, assessment: object):
        self.__assignments[assessment] = assessment


class Assessment(abc.ABC):
    def __init__(self, name, assessment_type, max_score):
        self.__name = name
        self.__type = assessment_type
        self.__max_score = max_score

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_max_score(self):
        return self.__max_score

    def set_name(self, new_name):
        self.__name = new_name
        return self.__name

    def set_type(self, new_type):
        self.__type = new_type
        return self.__type

    def set_max_score(self, new_score):
        self.__max_score = new_score
        return self.__max_score

    @abc.abstractmethod
    def add_score(self):
        pass


class Assignments(Assessment, ABC):
    def __init__(self, name, assignment_type, max_score):
        super().__init__(name, assignment_type, max_score)
        self.__score = {}

    def get_score(self):
        self.__score

    def add_score(self, student: object, score):
        self.__score[student] = score


class Exams(Assessment, ABC):
    def __init__(self, name, assignment_type, max_score):
        super().__init__(name, assignment_type, max_score)
        self.__score = {}

    def get_score(self):
        self.__score

    def add_score(self, student: object, score):
        self.__score[student] = score


class Homework(Assignments, ABC):
    def __init__(self, name, assignment_type, max_score):
        super().__init__(name, assignment_type, max_score)
        self.__score = {}

    def get_score(self):
        self.__score

    def add_score(self, student: object, score):
        self.__score[student] = score


class Grader:
    @staticmethod
    def calculate_average(scores):
        if not scores:
            return 0
        return sum(scores.values()) / len(scores)


class GradingSystem:
    def __init__(self):
        self.students = []
        self.instructors = []
        self.courses = []

    def add_student(self, student: object):
        self.students.append(student)

    def add_course(self, course: object):
        self.courses.append(course)

    def add_instructor(self, instructor: object):
        self.instructors.append(instructor)

    def enroll_student_in_course(self, student: object, course: object):
        if student in self.students and course in self.courses:
            course.add_student(student)
            student.enroll_a_course(course)
        else:
            print("Student or Course not found")

    def assign_instructor_to_course(self, instructor: object, course: object):
        if instructor in self.instructors and course in self.courses:
            instructor.add_course(course)
            course.set_instructor(instructor)
        else:
            print("instructor or course not found ")

    def add_assessment_to_course(self, assessment: object, course: object):
        if course in self.courses:
            course.add_assessment(assessment)
        else:
            print("assessment or course not found")

    def add_score_to_assessment(self, student, assessment, score):
        if student in self.students:
            assessment.add_score(student, score)
        else:
            print("student not found")


grading_system = GradingSystem()
# Create instructors
instructor1 = Instructor("Mohammad", 45, "mohammad@gmail.com", 1)
instructor2 = Instructor("Ghada", 45, "ghada@gmail.com", 2)
# Create students
student1 = Student("Hasan", 25, "hasan@gmail.com", "cs", 1)
student2 = Student("Sajed", 18, "sajed@gmail.com", "Doctor", 2)

# Create courses
course1 = Course("Python", instructor1)
course2 = Course("Anatomi", instructor2)

# Add instructors to the grading system
grading_system.add_instructor(instructor1)
grading_system.add_instructor(instructor2)

# Add students to the grading system
grading_system.add_student(student1)
grading_system.add_student(student1)

# Add courses to the grading system
grading_system.add_course(course1)
grading_system.add_course(course2)

# Enroll students in courses
grading_system.enroll_student_in_course(student1, course1)
grading_system.enroll_student_in_course(student2, course2)

# Assign instructors to courses
grading_system.assign_instructor_to_course(instructor1, course1)
grading_system.assign_instructor_to_course(instructor2, course2)

# Create assignments
assignment = Assignments("practical", "assignment", 100)
exam = Exams("final", "exam", 100)
homework = Homework("hw1", "homework", 10)

# Add assignments to courses
grading_system.add_assessment_to_course(assignment, course1)
grading_system.add_assessment_to_course(exam, course2)

# Add scores to assignments
grading_system.add_score_to_assessment(student1, assignment, 65)
grading_system.add_score_to_assessment(student2, exam, 86)

# Calculate student averages
avg1 = Grader.calculate_average(assignment.get_score())
avg2 = Grader.calculate_average(exam.get_score())

print(f"Average score for {assignment.get_name()}: {avg1}")
print(f"Average score for {exam.get_name()}: {avg2}")
