import requests
import json
import jsonpath
url="https://reqres.in/api/users"
file=open("C:\\Users\\prabeena.panda\\PycharmProjects\\API\\input.json",'r')
ip=file.read()
jin=json.loads(ip)
response=requests.post(url,jin)
print(response.content)
print(response.status_code)
assert response.status_code == 201
print(response.headers)
print(response.headers.get("Content-Length"))
res=json.loads(response.text)
id=jsonpath.jsonpath(res,'createdAt')
print(id)

