# Find maximum length sub-list in a nested list
def Find(lst):
    maxList = max((x) for x in lst)
    maxLength = max(len(x) for x in lst)
    return maxList, maxLength
lst = [['A'], ['A', 'B'], ['A', 'B', 'C']]
print(Find(lst))