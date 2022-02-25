import pandas as pd
nba = pd.read_csv('nba.csv')
nba.head()
nba.tail(10)
nba.shape
d=nba.dtypes
d
des = nba.describe()
print(des)
nba.mean()
df2 = nba["Age"].mean()
print(df2)
