"""This program aims to apply abstraction and inheritance between Employee class and Manager class, Employee class
have a method get_salary(), abd manager has to implement this method and add the bonus"""
import abc


class Employee(abc.ABC):
    def __init__(self, name, salary, role):
        self.__name = name
        self.__salary = salary
        self.__role = role

    # getter and setter

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name.title()

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary.title()

    def get_role(self):
        return self.__role

    def set_role(self, new_role):
        self.__role = new_role.title()


class Manager(Employee):
    def __init__(self, name, salary, role, bonus):
        super().__init__(name, salary, role)
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_salary(self):
        base_salary = super().get_salary()
        return base_salary + self.__bonus


# create instances of Employee and Manager
employee = Employee("John Doe", 50000, "Developer")
manager = Manager("Jane Smith", 100000, "Manager", 5000)

# get salary of employee and manager
print("Salary of employee:", employee.get_salary())
print("Salary of manager:", manager.get_salary())
print("Bonus of manager:", manager.get_bonus())
