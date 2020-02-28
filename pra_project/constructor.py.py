# Write a class and constructor to create an instances like below
# a. p1 = person(id=1,name=”ashok”,age=23,sal=56787)
# b. p2 = person(id=2,age=24,adhar=23456)
# c. p3 = person(id=4,pan=”brcp3456”,sal=23,age=45)

class Person:
    def __init__(self, id, **kwargs):
        self.id = id
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])




p1 = Person(id=1,name= 'ashok',age=23,sal=56787)
p2 = Person(id=2,age=24,adhar=23456)
p3 = Person(id=4,pan='brcp3456',sal=23,age=45)

