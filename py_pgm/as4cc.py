#same as as4
a={'classes':[{'python':[{'nag':['07:00am','02:00pm','04:00am','10:00pm']},\
        {'siva':['10:00am','05:00pm']}]},{'django':[{'nag':['11:00am','01:00pm']}]}]}
pc=0
nc=0
dc=0
sc=0
mc=0
#sub='am'
for c in a['classes']:
    if 'python' in c.keys():
        for p in c['python']:
            pk=p.keys()
           # print(pk)
            pc+=sum([len(x) for x in p.values()])
            for cls in pk:
                #print(cls)
                if cls =='nag':
                    nc+=len(p[cls])
                    for cl in p[cls]:
                        #print(cl)
                        if cl.endswith('am'):#if sub in cl:
                            mc+=1
                if cls =='siva':
                    sc+=len(p[cls])
                    for cl in p[cls]:
                        if cl.endswith('am'):#if sub in cl:
                            mc+=1
    if 'django' in c.keys():
        for d in c['django']:
            #print(d)
            dk=d.keys()
            #print(dk)
            dc+=sum([len(x) for x in d.values()])
            for cls in dk:
                if cls=='nag':
                    nc+=len(d[cls])
                    for cl in d[cls]:
                        if cl.endswith('am'):#if sub in cl:
                            mc+=1
print(pc)
print(nc)
print(sc)
print(dc)
print(mc)