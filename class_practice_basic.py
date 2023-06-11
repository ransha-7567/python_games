'''
In Python, a class is a blueprint for creating objects (instances) that have specific properties (attributes) and
behaviors (methods). It defines a new data type with its own characteristics and functionality.

A class encapsulates related data and functions into a single unit, allowing for code organization, reusability, and
abstraction. Objects created from a class are instances of that class and have access to its attributes and methods.

Here's an example of a simple class in Python:

'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("The car engine is starting.")

    def drive(self, distance):
        print(f"The car is driving for {distance} miles.")

    def stop_engine(self):
        print("The car engine is stopping.")
"""
In this example, we define a Car class. The class has three attributes (make, model, and year) and three methods 
(start_engine(), drive(), and stop_engine()).

The __init__() method is a special method known as the constructor. It is called when a new instance of the class is 
created. It initializes the object's attributes (make, model, and year) with the values passed as arguments.

The start_engine(), drive(), and stop_engine() methods define the behavior of the Car class. They can be invoked on an 
instance of the class to perform specific actions related to the car object.

To create an object (instance) of the Car class, we can use the following code:

"""

my_car = Car("Toyota", "Camry", 2022)

'''
Here, my_car is an instance of the Car class, created with the provided values for make, model, and year. We can then 
access the attributes and call the methods of the my_car object:

'''
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)  # Output: 2022

my_car.start_engine()  # Output: The car engine is starting.
my_car.drive(60)  # Output: The car is driving for 60 miles.
my_car.stop_engine()  # Output: The car engine is stopping.

'''
By using classes, we can create multiple objects (instances) of the same class, each with its own set of attributes and 
behaviors. Classes provide a way to define reusable and modular code, facilitating object-oriented programming 
principles such as encapsulation, inheritance, and polymorphism.
'''