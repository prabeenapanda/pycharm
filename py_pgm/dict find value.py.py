# find how many classes of python,django,nag and morning class
nc = 0
pc = 0
dc = 0
mc = 0
a = {'classes':[{'python':[{'nag':['07:00am','02:00pm','04:00pm','10:00pm']},\
                {'siva':['10:00am','05:00pm']}]},{'django':[{'nag':['11:00am','01:00pm']}]}]}
for c in a['classes']:
    if 'python' in c.keys():
        for p in c['python']:
            pc+=sum([len(x) for x in p.values()])
            if 'nag' in p.keys():
                for cls in p['nag']:
                   print(cls)
                   nc += 1
                   if cls.endswith("am"):
                       mc += 1
            if 'siva' in p.keys():
                for cls in p['siva']:
                    if cls.endswith("am"):
                       mc += 1
    if 'django' in c.keys():
        for d in c['django']:
            dc += sum([len(x) for x in d.values()])
            for cls in d['nag']:
                nc += 1
                if cls.endswith("am"):
                         mc += 1
print("nag_classes:",nc)
print("python_classes:",pc)
print("django_classes:",dc)
print("morning_classes:",mc)