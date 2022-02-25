import requests
import json
url="https://jsonplaceholder.typicode.com/todos/10"
data={'id':10,'userid':1,'address+pincode':'pondy 605004','completed':'True'}
headers={'content-Type':'application/json; charset=UTF-8'}
res=requests.put(url.data=json.dumps(data),headers=headers)
print(res.status_code)
print(res.ok)
print(res.content)
print(res.text)
print(type(res.text))
print(res.url)
print(res.headers['content-Type'])
print(res.encoding)
