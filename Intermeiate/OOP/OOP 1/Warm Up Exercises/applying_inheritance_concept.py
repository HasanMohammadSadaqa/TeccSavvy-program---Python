"""
This program aims to applying inheritance concept by creating two classes: Person, Student(inherits from Person class)
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = int(student_id)

    def enroll(self, course):
        print(f"Enrolling {course} for {self.get_name()}(ID: {self.__student_id})")


student = Student("Hasan", 25, 123)
student.enroll("Math")
