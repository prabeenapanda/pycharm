
class Employee:
    COMPANY = "Gss"     #SHARABLE object it means it is fixed or same for all employess this is also called the class variables.
    emp_count = 0         #SHARABLE,MODIFIABLE
    '''Class constructor or Initialization method'''
    def __init__(self, id, name, sal):     # constructors is used to define the variables.here init is the constructor, here self is instance variable(A variable that is defined inside a method and belongs only to the current instance of a class. )
            self.id=id                #instance variable  ,local variable here self.id is instance variable means it will create the memory location and store the values permanently.
            self.name=name           # here name is loacal variable
            self.sal=sal
            Employee.emp_count += 1
    def get_emp_details(self):
        #import pdb;pdb.set_trace()
        print("EMP DETAILS ARE : ",self.id," ",self.name," ",self.sal)
        print("Employee count ",Employee.emp_count)

giri = Employee(10, "Giri A", 1000)
COMPANY = "sungard"#if u try to modify the class variable like this it wont be modified
Employee.COMPANY = "sungard"#like this if u write it will be modified for all instance
print(giri.COMPANY)
Arun = Employee(20,"Arun",20000)
print(Arun.COMPANY)
print(id(giri.COMPANY) == id(Arun.COMPANY)) #same so true
#print("---------Normal Instance calling-------------")
giri.get_emp_details() # this two methods are same to get the value
Employee.get_emp_details(giri)
#print("------Instance method calling with className------")
print("GET attribute name ",getattr(giri, "name"))        #these are like CRUD
print("SET attribute name ",setattr(giri, "name", "MAD")) # SETTER -create it will only set but wont print
print("GET attribute name ",getattr(giri, "name"))        # GETTER -update
print("HAS attribute sal ",hasattr(giri, "address"))       # HAS   - read
#print(delattr(giri, "sal"))                               # DELETE - delete
print("AFter deleting ",giri.sal) # here it will give the error because sal attribute is already deleted
print("HAS attribute sal ",hasattr(giri, "sal"))  # here it will check perticular object is there or not.
#some inbuilt functions for attribute
print("Employee.__dict__:", Employee.__dict__)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
