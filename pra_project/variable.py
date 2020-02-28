p=[10,20,30]
pp=[10,20]
def fuu(r,q):
    r=[10]
    r.append(40)
    print(r)#[10,40]
    q.append(50)
    print(q) #[10,20,50]
fuu(p,pp)
print(p) # this is not affected at all [10,20,30]
print(pp)#[this will be affected as both pp and q refer to same memory location [10,20,50]
#print(r)#error as r is local we can not call outside



a=[1,2,3]
def fun(b):
    global a
    b=[10]
    b.append(40)
    print(b)
    a=[5,7] #here the value is changing
    a.append(6)
fun(a)
print(a)

#if u are declaring somthing global or nonlocal and changing that inside the fun it will be changed for outside also
#global varible will be outside of the function and nonlocal varible should be in the outer function
#outside of inner function means for non local nested function is needed
#in both the cases the value will be over written if u change.



def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x) #for this also the value is changing
outer()