# OOP is a programming paradigm based on the concept of "objects",
# which can contain data, in the form of fields, often known as attributes;
# and code, in the form of procedures, often known as methods.

# attributes are data stored inside a class or instance and represent the state or
# quality of the class or instance. In short, attributes store information about the instance.

# methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

# class is a blueprint for the object. It contains all the methods and attributes.

class Car:
    """A simple attempt to represent a car."""
    # __init__ is a special method that Python runs automatically
    # whenever we create a new instance based on the car class.
    # self is a reference to the instance itself.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    # The self parameter is required in the method definition,
    # and it must come first before the other parameters.

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()