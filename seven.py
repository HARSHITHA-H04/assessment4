import requests as reqs
import pandas as pd
response=reqs.get('http://jsonplaceholder.typicode.com/todos/10')
print(respose.status_code)
print(response.text)
