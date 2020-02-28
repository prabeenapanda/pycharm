#combine nested list to tuple list
list1 = [[1, 4, 5], [8, 7], [2]]
list2 = [['g', 'f', 'g'], ['f', 'r'], ['u']]
res = [(u, v) for x, y in zip(list1,list2) for u, v in zip(x, y)]# its a  nested we hae to go inside so give 2 time
print(res)

