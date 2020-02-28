import requests
import json
import jsonpath
url="https://reqres.in/api/users"
file=open("C:\\Users\\prabeena.panda\\PycharmProjects\\API\\input.json",'r')
ip=file.read()
jin=json.loads(ip)
response=requests.put(url,jin)
print(response.content)
print(response.status_code)
res=json.loads(response.text)
at=jsonpath.jsonpath(res,"updatedAt")
print(at)
#in put there won't be any id and there will be updatedat over there to differenciate.