#22 call parent create method in child class method create. reffer the below code.
class C1:
    def create(self):
        print("create method")
class C2(C1):
    def create(self):
        print("child class create method definition")
        # how to call parent class create method here?
        super().create()

obj1 = C2()
obj1.create()
