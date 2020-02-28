import pandas as pd
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(left, right, on='key')
print(result)
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                 'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on=['key1', 'key2'])
print(res)
re = pd.merge(left, right, how='left', on=['key1', 'key2'])
#re = pd.merge(left, right, how='right', on=['key1', 'key2'])
#re = pd.merge(left, right, how='outer', on=['key1', 'key2'])
#re = pd.merge(left, right, how='inner', on=['key1', 'key2'])
print(re)
df1=pd.DataFrame({"visitors":[20,30,40,50,60],"rate":[20,40,50,80,10],"grp":[50,1,3,6,5]},index=[1,2,3,4,5])
df2=pd.DataFrame({"visitors":[20,30,40,50,60],"rate":[20,40,50,80,10],"grp":[50,1,3,6,5]},index=[6,7,8,9,10])
mer=pd.merge(df1,df2)
#print(mer)
#only based on that it will be merged other rows will be repeated
merr=pd.merge(df1,df2, on = "rate")
print(merr)
