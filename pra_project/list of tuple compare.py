#arrange in descending order marks
l=[("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)]
l.sort(reverse=True, key = lambda x: x[1])
print(l)

#or
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (sub_li[j][1] < sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li

sub_li = [("mohan", 80), ("satish", 90), ("purnesh", 40), ("venkat", 30)]
print(Sort(sub_li))


