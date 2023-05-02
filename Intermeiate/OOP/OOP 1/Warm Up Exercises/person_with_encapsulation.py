"""
applying encapsulation concept
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

    def birthday(self):
        self.__age += 1


person = Person("Hasan", 25)
person.birthday()
print(person.get_age())
