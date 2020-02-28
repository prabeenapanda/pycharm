#as4 q modification
a={'classes':{'python':[{'nag':[{'am':['1','2','3']},{'pm':['1','2','3']}]},
                         {'siva':['10','05']}],}}
pc=0
nc=0
cc=0
#if it is nested dictionary we have to go like this
for c in a.values():
    print(c)
    for p in c.values():
        print(p)
        pc+=1    #a dictinary will have only value for one key
    for q in c['python']:
        print(q)
#this code below is for original question
    #if 'python' in c.keys():
        #for p in c['python']:
             # pc+=sum([len(x) for x in p.values()])
              #if 'nag' in p.keys():
                   #for n in p['nag']:
                        #nc+=sum([len(x) for x in n.values()])
                       # if 'am' in n.keys():
                            #for cls in n['am']:
                               # cc+=1
print(pc)
print(nc)
print(cc)