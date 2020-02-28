#from more_itertools import flatten

l = [10, 20, 30, [40,[1,23], 50, 60], 70, [80, 90, 20]]
#print(list(flatten(l)))
newl = []
def my_fun(l):
    for ele in l:
        if type(ele) == list:
            my_fun(ele)
        else:
            newl.append(ele)

my_fun(l)
print(newl)

