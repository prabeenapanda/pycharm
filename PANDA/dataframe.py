import pandas as pd
data={"day":[1,2,3,4,5],"visitors":[200,300,400,500,600],"rate":[20,40,50,80,10]}
df=pd.DataFrame(data)
print(df)
#slicing
print(df.tail(2))
print(df.head(2))
print(df.describe())
#An excellent practice to get a clue about the data is to use describe().
# It provides the counts, mean, std, min, max and percentile of the dataset.
print(df[['day', 'rate']]) #slicing only those values will be printed
print(df[0:3])
print(df.iloc[:, :2])#slicing using index instead of col name
#df.drop(columns=['day', 'rate']) #to delete the cols
#print(df)
#merging
#index is not user defined it is inbuilt col
print(df.sort_values("rate"))#sort based on rate
df.rename(columns={"day":"date", "rate": "price"})
print(df)



