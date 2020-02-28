# What is an inheritance? write an example program to demonstrate inheritance.
# Inheritance is a mechanism in OOPs where one class inherits the properties and methods of another.
# the inherited class will have have its own property and methods.
#the init method of super class wont go to child class automatically we have to call the using parent
# class name or super() and its not manadatory to call that in init of child class only
class Person:
    name = ""
    age = 0


    def __init__(self, name, age):
        self.name = name
        self.age = age



    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)


class Student(Person):
    studentId = ""

    def __init__(self, name, age,id):
        Person.__init__(self, name, age)
        #or super().__init__(name, age)
        self.id = id

    def getId(self):
        return self.id



person1 = Person("Richard", 23)
person1.showAge()

student1 = Student("Max", 22, "102")
print(student1.getId())
student1.showName()