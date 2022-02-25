import requests
url="https://jsonplaceholder.typicode.com/todos/7"
res=requests.delete(url)
res.json()
res.status_code
