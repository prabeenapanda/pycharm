class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
person1=person("prabeena",22)
print(person1.name)#error bcoz private
print(person1.age)#error bcoz diff access specifier
class cup():
    def __init__(self,color,design):
        self._color=color
        self._design=design
cup1=cup("white","flower")
print(cup1._color)#white no error
print(cup1._design)#error at the time of calling the object should be same as access specifier
class me:#if u want to print private varibale create the object for the class
         # before nd call with that object
    def __init__(self):
        self.__name="prabeena"
        self.__salry=25000
p=me()
class me:
    def __init__(self):
        self.__name="prabeena"
        self.__salary=25000
    print(p.__name,p.__salry)#if we try to print it dirctly with out creating any object
                   # for the class then it will show an error

