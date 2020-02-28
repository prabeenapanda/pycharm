# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
   stream = 'cse'				 # Class Variable
   def __init__(self,name,roll):
      self.name = name#instance variable
      self.roll = roll#instance variable


   def string(self):
     return f"{self.name} {self.roll}"
# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name,a.roll) # prints "Geek 1"
print(b.roll) # prints 2"
print(CSStudent.string(a))

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"
#getitem dunder use
class GetTest(object):
   def __init__(self):
      self.info = {
         'name': 'Prabeena',
         'country': 'India',
         'number': 12345812
      }

   def __getitem__(self, i):
      return self.info[i]


foo = GetTest()

print(foo['name'])
# Output: 'Yasoob'

print(foo['number'])
# Output: 12345812

