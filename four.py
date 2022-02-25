import pandas as pd
m=pd.read_csv('matches.csv')
m.head()
print(m.columns.tolist())
nan()
m
df1=pd.DataFrame(m.values[m['win_by_wickets'].notnull()])
df1
df1.mean()
df1.std()
m[['city','winner']]
