class per:
    def __init__(self): # constructor
        self.__name="Unknown" # instance attribute show error because private
        self._age=0 # instance attribute protected but will not show error
p=per()
print(p.__name)
print(p._age)
class pers:#giving default value to attribute
    def __init__(self, name="rajat", age=23):
        self.name=name
        self.age=age
c=pers()
print(c.name)
print(c.age)
class pe:#class attribute
    greet='Hello!'
print(pe.greet)
e=pe()
print(e.greet)
class person:
    totalObjects=0
    def __init__(self):
        person.totalObjects=person.totalObjects+1
p1=person()
print(p1.totalObjects)
p2=person()
print(p2.totalObjects)

