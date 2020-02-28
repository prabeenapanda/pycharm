class c1:
    def fun(self):
        print("hi")
class c2(c1):
    def func(self):
        print("hiiiii")
class c3(c2):
    def funct(self):
        print("hello")
class c4(c2,c3):
    def function(self):
        print("gd")
c=c4()
c.fun()