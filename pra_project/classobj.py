#class that can create only one object.IF create one more object then it should written existing object
# but not new.Create three instances and print id’s of the instances.All the id’s should show same address.
class Shark:
    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")

sammy = Shark()
sammy.swim()
sammy.be_awesome()
