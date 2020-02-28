import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print(key,value)
for row_index,row in df.iterrows():
   print(row_index,row)
for row in df.itertuples():
    print(row)
unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df=unsorted_df.sort_index()
print(sorted_df)
sorted = unsorted_df.sort_index(ascending=False)
print(sorted)
sort=unsorted_df.sort_index(axis=1)
print(sort)#output will come like col then col2
unsorted = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sor = unsorted.sort_values(by='col1')
print(sor)

