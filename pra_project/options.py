def option(input,correct,option):
    lis=[]
    for i in input:
        if i in correct:
            lis.append(1)
        if i not in correct:
            lis.append(0)
        if i not in option:
            print("no such option")
    if sum(lis) == 0:
        print("wrong")
    elif sum(lis) == 2:
        print("right")
    elif sum(lis) == 1:
        print("partially right")
option([1,2],[3,4],[1,2,3,4])
