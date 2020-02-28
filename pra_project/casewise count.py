l = ['a', 'A', 'b', 'B', 'd', 'D', 'c', 'C']
for i in set(l):
    I=i.casefold()
    c=0
    for j in l:
         if i.casefold()==j.casefold():
              c += 1
              if l.count('I')==1:
                     print("count of",i.casefold(),"is",c)
              else:
                     pass

