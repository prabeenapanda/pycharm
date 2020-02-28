#take 2 string and true if they have element in common
def list(lis1,lis2):
    for x in lis1:
        for y in lis2:
            if x==y:
                return "true"
            else:
                return "false"
print(list([1,2,3],[3,4,5]))
print(list([26,76,98],[12,34,67]))



