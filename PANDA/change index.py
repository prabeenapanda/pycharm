import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df = pd.DataFrame({"visitors":[20,30,40,50,60],"rate":[20,40,50,80,10],"grp":[50,1,3,6,5]},index=[1,2,3,4,5])
#df.set_index("rate",inplace=True) #it make a as index
df=df.rename(columns={"visitors":"users"})
print(df)
df.plot()
plt.show()
