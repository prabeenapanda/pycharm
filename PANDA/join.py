import pandas as pd
df1=pd.DataFrame({"person":[2,3,4,5,6],"time":[20,40,50,80,10]},
                 index=[1,2,3,4,5])
df2=pd.DataFrame({"visitors":[20,30,40,50,60],"rate":[2,4,5,8,1]},
                 index=[1,2,3,4,4])
joined=df1.join(df2, how='outer')
print(joined)
joi=df1.join(df2, how='inner')
print(joi)
#joining on key
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                                   'key': ['K0', 'K1', 'K0', 'K1']})

right = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                       index=['K0', 'K1'])
#Take the union of them all, join='outer'. This is the default option as it results in zero information loss.

#Take the intersection, join='inner'.

result = left.join(right, on='key')
print(result)