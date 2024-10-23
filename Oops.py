class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):  # Add double underscores to __init__
        self.name = name
        self.age = age
        self.__age=age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return f"{self.name} is {self.age} years old."

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1.bark())
print(dog2.get_age())
print(dog1.species)


class Cat:
    species = "Felis catus"

    def __init__(self, name, age):  # Add double underscores to __init__
        self.name = name
        self.age = age
        self.__age=age

    def meew(self):
        return f"{self.name} says meeeeeoooowwww!"

    def get_age(self):
        return f"{self.name} is {self.age} years old."

# Creating instances of the Dog class
cat1 = Cat("Billi", 3)
cat2 = Cat("Bilota", 5)

print(cat1.meew())
print(cat2.get_age())
print(cat1.species)

class Animal:
    def __init__(self,name,age):
        self.name()
        self.age()
        self.__age=age #private
    
    def get_age(self):
        return f"{self.name} is {self.age} years old."
    def __str__(self):
        return f"\nname is {self.name}\n age is {self.__age}"
    
from animal import Animal

class Dog(Animal):
        def bark(self):
            return f"{self.name} says woof!"

from dog import dog
dog1=Dog("d1",3)
cat1=Cat("c1",4)