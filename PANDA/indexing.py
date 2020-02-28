import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print(df.loc[:,'A'])
print(df.loc[:,['A','C']])
print(df.loc[['a','b','f','h'],['A','C']])
print(df.loc['a':'h'])
print(df.loc['a']>0)
#indexing
print(df.iloc[:4])
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])
print(df.iloc[[1, 3, 5], [1, 3]])
print(df.iloc[1:3, :])
print(df.iloc[:,1:3])


df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print(df.ix[:4])
print(df.ix[:,'A'])
print(df[['A','B']])
print(df[2:2])
print(df.A)