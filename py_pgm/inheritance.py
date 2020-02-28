class parent:
    def fun(self):
        print("hi")
class child(parent):
    def met(self):
        print("hello")

c1=child()
c1.fun()