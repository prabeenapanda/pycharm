def sort_list(func):
    def inner(l):
        for i in range(len(l)-1,0,-1):
            for j in range(i):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
        return func(l)
    return inner
@sort_list
def get_list(lst):
    return lst
l = [3, 65, 3, 2, 98, 4, 5, 6, 6, 34, 87]
sorted_list = get_list(l)
print(sorted_list)

