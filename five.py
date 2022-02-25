import requests as reqs
import pandas as pd

url='http://jsonplaceholder.typicode.com/todos'
response=reqs.get(url)
df=pd.DataFrame(response)
df.head()
df.head(7)
