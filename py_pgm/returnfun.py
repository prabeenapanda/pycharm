def Parent(num):
    def fchild():
        return "hi"
    def schild():
        return "hello"
    if num==1:
        return fchild()
    else:
        return schild
first=Parent(1)
print(first)
#print(first())
second=Parent(2)
print(second) #memory address
print(second())

#using try except
def parent(num):

    def first_child(num1,num2):
        return "Printing from the first_child() function.",num1,num2
    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num== 10
        print(first_child(2,3))
    except AssertionError as a:
        print(second_child())#print the output
        print(second_child)#print the address

foo = parent(10)
bar = parent(11)