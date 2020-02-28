class Clist:

    def __init__(self,l):
        self.list1 = l

    def __add__(self, other):
        result =  [x+y for x,y in zip(self.list1, other.list1)]
        return result


l1 = Clist([1,2,3])
l2 = Clist([2,3,4])

print(l1+l2)





