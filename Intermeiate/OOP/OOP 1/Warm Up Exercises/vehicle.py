"""Create a Vehicle class with attributes make, model, and year. Add a method get_info() that returns a string with
the vehicle's make, model, and year. Then create a Car class that inherits from Vehicle and adds a method accelerate(
speed) that prints the message "The car is accelerating to {speed} mph"."""


class Vehicle:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_info(self):
        return f"{self.__year} {self.__make} {self.__model}"


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def accelerate(self, speed):
        print(f"The car is accelerating to {speed} mph")


car = Car("Toyota", "Corolla", 2021)
print(car.get_info())
car.accelerate(60)
