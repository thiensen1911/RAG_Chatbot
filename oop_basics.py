# OOP (Object-Oriented Programming) in Python
# OOP lets us organize code ussing classes and objects.
# A class is a blueprint, and an object is an instance of that class.

class Animal:
    # __init__() is the constructor. It sets up the object when created.
    def __init__(self, name, species):
        self.name = name        # attribute (data)
        self.species = species  # attribute (data)
        self.hunger = 0         # attribute (data)

    # this is a method. It defines what the object can do
    def eat(self):
        self.hunger = max(0, self.hunger - 1)
        return f"(self.name) eats. Hunger now : {self.hunger}"

    def speak(self):
        return f"{self.name} make a sound." # this will be overridden

# Inheritance: Dog is a child class of Animal
class Dog(Animal):
    def speak(self): # Overriding the parent method (polymorphism)
        return f"{self.name} barks!"

# class objects (instances)
cat = Animal("Whiskers", "Cat")
dog = Dog("Buddy", "Dog")

# Using the objects
print(cat.speak()) # Output: Whiskers make a sound.
print(dog.speak()) # Output: Buddy barks!
print(cat.eat())   # Output: Whiskers eats. Hunger now : 0 
print(dog.eat())   # Output: Buddy eats. Hunger now : 0

# Key OOP Concepts:
# 1. Class - blueprint for creanting objects
# 2. Object - instance of a class
# 3. Attributes - data (name, species, hunger)
# 4. Methods - behavior (eat, speak)
# 5. Inheritance - child class gets parent's features
# 6. Polymorphism - name method, different behavior 

# MYRAKON_LAB