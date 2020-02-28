# What is the difference among dict.items(), dict.iteritems(), dict.viewitems()? Elaborate with an example.
# dict.items() return list of tuples, and dict.iteritems() return iterator object of tuple in dictionary as (key,value)

#  dict.iteritems(), dict.viewitems() are depricated and removed in Python 3

d={1:'one',2:'two',3:'three'}
print('d.items():')
for k,v in d.items():
   if d[k] is v: print('\tthey are the same object')
   else: print('\tthey are different')

print('d.iteritems():')
for k,v in d.iteritems():
   if d[k] is v: print('\tthey are the same object')
   else: print('\tthey are different')