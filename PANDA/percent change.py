#Series, DatFrames and Panel, all have the function pct_change().
# This function compares every element with its prior element and computes the change percentage.
import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())
df = pd.DataFrame(np.random.randn(5, 2))
print(df.pct_change())
#Covariance is applied on series data. The Series object has a method cov to compute
# covariance between series objects. NA will be excluded automatically.
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())
#Correlation shows the linear relationship between any two array of values (series).
# There are multiple methods to compute the correlation like pearson(default), spearman and kendall.
print(frame['a'].corr(frame['b']))
#Data Ranking produces ranking for each element in the array of elements.
# In case of ties, assigns the mean rank.

s = pd.Series(np.random.randn(5), index=list('abcde'))
s['d'] = s['b'] # so there's a tie
print(s.rank())