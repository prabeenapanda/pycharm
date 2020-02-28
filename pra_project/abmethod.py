# Python program showing
# abstract class cannot
# be an instantiation
from abc import ABC,abstractmethod

class Animal(ABC):
	@abstractmethod
	def move(self):
		print("hi")
class Human(Animal):
	def move(self):
		super().move()
		print("I can walk and run")

class Snake(Animal):
	def move(self):
		super().move()
		print("I can crawl")

class Dog(Animal):
	def move(self):
		print("I can bark")

class Lion(Animal):
	def move(self):
		print("I can roar")

s=Snake()
s.move()
h=Human()
h.move()


