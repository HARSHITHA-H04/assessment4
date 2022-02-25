import requests as reqs
import pandas as pd
data={"userid":10,"title","mocoroni","completed":"false"}
response=reqs.post(url.data)
df1=pd.DataFrame(response)
df1
