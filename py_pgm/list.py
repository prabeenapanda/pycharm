l=[0,[1,2,3],[4,5,[6,7,8],9,10],[11,[12,[13,14,15],[16,17],18]]]
output=[]
def nesting(l):
    for i in l:
        if type(i) == list:
            nesting(i)
        else:
            output.append(i)
print ('The original list: ', l)
nesting(l)
print ('The list after removing nesting: ', output)


