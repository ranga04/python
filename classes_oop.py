# classes_oop.py
# This file demonstrates object-oriented programming in Python.

# =====================
# 1. Basic Class Definition
# =====================

class Person:
    """A simple class representing a person."""

    # Constructor (__init__) method to initialize an object
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    # Method to print a greeting
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.

# =====================
# 2. Instance and Class Variables
# =====================

class Employee:
    """Class to represent an employee with a common 'company' attribute."""
    
    company = "TechCorp"  # Class variable, shared by all instances

    def __init__(self, name, salary):
        self.name = name     # Instance variable
        self.salary = salary # Instance variable

# Accessing instance and class variables
emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)
print(emp1.company)   # Output: TechCorp (shared class variable)
print(emp2.salary)    # Output: 60000 (unique to emp2)

# =====================
# 3. Methods
# =====================

class Calculator:
    """Class that provides methods for basic calculations."""

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

calc = Calculator()
print(f"Addition: {calc.add(10, 5)}")        # Output: 15
print(f"Subtraction: {calc.subtract(10, 5)}") # Output: 5

# =====================
# 4. Class Methods and Static Methods
# =====================

class MathOperations:
    """Class with class and static methods."""

    # Class method
    @classmethod
    def multiply(cls, x, y):
        return x * y

    # Static method
    @staticmethod
    def power(base, exponent):
        return base ** exponent

print(f"Multiplication (Class Method): {MathOperations.multiply(3, 4)}")  # Output: 12
print(f"Power (Static Method): {MathOperations.power(2, 3)}")            # Output: 8

# =====================
# 5. Inheritance
# =====================

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic Animal Sound"

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call to the parent constructor
        self.breed = breed

    # Method overriding
    def make_sound(self):
        return "Woof!"

dog = Dog("Buddy", "Golden Retriever")
print(f"{dog.name} says {dog.make_sound()}")  # Output: Buddy says Woof!

# =====================
# 6. Encapsulation and Private Variables
# =====================

class BankAccount:
    """Class with encapsulated (private) attributes."""

    def __init__(self, owner, balance):
        self.owner = owner            # Public attribute
        self.__balance = balance       # Private attribute (by convention with __)

    # Public method to access the private variable
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(f"Balance: {account.get_balance()}")  # Output: 1000
# print(account.__balance)  # Would raise an AttributeError

# =====================
# 7. Polymorphism
# =====================

# Example with polymorphism through method overriding
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog("Rex", "Labrador"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name} makes sound: {animal.make_sound()}")

# =====================
# 8. Magic (Dunder) Methods
# =====================

class Book:
    """Class demonstrating dunder (magic) methods."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    # __str__ method to define string representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    # __len__ method to define length (arbitrary example for demo purposes)
    def __len__(self):
        return len(self.title)

book = Book("1984", "George Orwell")
print(book)               # Output: 1984 by George Orwell
print(f"Title Length: {len(book)}")  # Output: 4

# =====================
# 9. Inheritance and Overriding
# =====================

# Parent class
class Vehicle:
    def description(self):
        return "This is a vehicle."

# Child class
class Car(Vehicle):
    def description(self):
        return "This is a car."

# Another child class
class Truck(Vehicle):
    def description(self):
        return "This is a truck."

vehicles = [Vehicle(), Car(), Truck()]
for v in vehicles:
    print(v.description())

# =====================
# End of classes_oop.py
# =====================
