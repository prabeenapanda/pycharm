import requests
import json
import jsonpath
url="https://reqres.in/api/users"
response=requests.delete(url)
print(response.status_code)
#if its deleted the the status will be 204
