#constructor inheritance
#if u try to do multilevel inheritance after that multiple inheritance that is not possible
#but if u try to do multiple inheritance after that multilevel  inheritance that is possible
#u can write n number of super in ur sub classes in multilevel inheritance
#super is used to use the parent class method in the child class method
#it runs through mro if that ans is found in the left most class it will not go to the class after that
#but if the ans is not found it will go after that claas method.
class A(object):
    def __init__(self):
        print("a")
    def fet1(self):
        print("1")
class D():
    def __init__(self):
        print("d")
    def fet2(self):
        print("2")
class E(A,D):
    def __init__(self):
        super().__init__()
        print("e")
    def fet3(self):
        print("1")
class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("b")
    def fet4(self):
        super().fet1()
        print("3")
    def fet5(self):
        print("4")
class C(B):
    def fet6(self):
        super(C,self).__init__()
        print("c")
c=C() #a b
c.fet6()#a b c
b=B()#a b
b.fet4()#1 3
e=E()#a e