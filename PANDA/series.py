import pandas as pd
import numpy as np
sr=pd.Series([1., 2., 3.])
print(sr)
srr=pd.Series([1., 2., 3.], index=['a', 'b', 'c'])
print(srr)
srrr=pd.Series([1,2,np.nan])
print(srrr)
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
sd = pd.Series(dictionary)
print(sd)
Data = [[2, 3, 4], [5, 6, 7]]
snd = pd.Series(Data)
print(snd)
s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])  # Define series 1
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])  # Define series 2
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])  # Define series 3
Data = {'first': s1, 'second': s2, 'third': s3}  # Define Data
dfseries = pd.DataFrame(Data)
print(dfseries)
import pandas as pd # Import Library
d1 =[[2, 3, 4], [5, 6, 7]] # Define 2d array 1
d2 =[[2, 4, 8], [1, 3, 9]] # Define 2d array 2
Data ={'first': d1, 'second': d2} # Define Data
df2d = pd.DataFrame(Data)
ss = pd.Series(5, index=[0, 1, 2, 3])
print(ss)
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s)
print(s[0])
print(s[:3])
print(s[-3:])
print(s['a'])
print(s[['a','c','d']])
#print(s['f'])
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df ['one'])
print(df["two"])
print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print(df['four'])
sss = pd.Series(np.random.randn(4))#it will select randomly
print(sss)
print ("The axes are:")
print(sss.axes)
print ("Is the Object empty?")
print(sss.empty)
print ("The dimensions of the object:")
print(sss.ndim)
print ("The size of the object:")
print(sss.size)
print ("The actual data series is:")
print (sss.values)
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}

#Create a DataFrame
df = pd.DataFrame(d)
print(df.sum())#the index value will be summed
print(df.sum(1))#the 1st index will be summed
print(df.mean())#it will give the mean value of the integer rows.
print(df.std())#will give the standar deviation
#describe function gives the mean, std and IQR values. And, function excludes the character columns and given summary about numeric columns. 'include' is the argument which is used to pass necessary information regarding what columns need to be considered for summarizing. Takes the list of values; by default, 'number'.

#object − Summarizes String columns
#number − Summarizes Numeric columns
#all − Summarizes all columns together (Should not pass it as a list value)

print(df.describe(include=['object']))
print(df.describe(include='all'))

