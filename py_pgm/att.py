
class sampleclass:
    count = 0  # class attribute if u change it in one instance everywhere the value will be changed

    def increase(self):
        sampleclass.count += 1

# Calling increase() on an object
s1 = sampleclass()
s1.increase()
print(s1.count)
# Calling increase on one more
# object
s2 = sampleclass()
s2.increase()
print(s2.count)
print(sampleclass.count)


# Python program to demonstrate
# instance attributes. if u change the value in one instance it won't affect any other instance
class emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)

e1 = emp("prabeena",25000)
e1.show()
print("Dictionary form :", vars(e1))  # displays the attribute of an instance in the form of an dictionary.
print(dir(e1))  # displays more attributes than vars function,as it is not limited to instance.
# It displays the class attributes as well.
