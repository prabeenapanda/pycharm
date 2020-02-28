class student():
    #self.m1=m1
    #self.m2=m2
    def __add__(self,other):
        self.m1=m1
        self.m2=m2
        print(self.m1)
        print(other.m2)
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s4=student(m1+m2)
        return s4
s1=student(2,6)