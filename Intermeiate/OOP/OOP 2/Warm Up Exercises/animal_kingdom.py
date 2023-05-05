"""Creating an abstract class called Animal. Defining two abstract methods called speak() and move() that
should be implemented by its subclasses. Creating three subclasses called Dog, Cat, and Fish. Implement the speak() and
move() methods for all three subclasses. Dogs and cats should be able to speak and move on land. Fish should be able
to speak and move in water."""
import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def speak(self):
        pass

    @abc.abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def speak(self):
        return "'Woff'"

    def move(self):
        return "Four legs."


class Cat(Animal):
    def speak(self):
        return "'Meow'"

    def move(self):
        return "Four legs."


class Fish(Animal):
    def speak(self):
        return "..."

    def move(self):
        return "swimming in water."


# create instances of Dog, Cat and Fish
dog = Dog()
cat = Cat()
fish = Fish()

# make the animals speak and move
print("Dog says:", dog.speak())
print("Dog moves by:", dog.move())
print("Cat says:", cat.speak())
print("Cat moves by:", cat.move())
print("Fish says:", fish.speak())
print("Fish moves by:", fish.move())
