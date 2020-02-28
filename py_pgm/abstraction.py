from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")

#Abstract classes are incomplete because they have methods which have no body.
# If python allows creating an object for abstract classes then using that object if anyone calls
# the abstract method
#https://www.geeksforgeeks.org/abstract-classes-in-python/
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Snake(Animal):
    def move(self):
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


c = Animal()