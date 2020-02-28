#Check if a nested list is a subset of another nested list
def checkSubset(list1, list2):
    exist = True
    for i in list2:
        if i not in list1:
            exist = False
    return exist
list1 = [[2, 3, 1], [4, 5], [6, 8]]
list2 = [[4, 5], [6, 9]]
print(checkSubset(list1, list2))