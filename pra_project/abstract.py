# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class R(ABC):
	def rk(self):
		print("Abstract Base Class")

class K(R):
	def rk(self):
		super().rk()
		print("subclass ")

# Driver code
r = K()
r.rk()

