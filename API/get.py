import requests
import json
import jsonpath
url="http://api.open-notify.org/astros.json"
response=requests.get(url)
#print(response.content)#shows the content
#print(response.status_code)#shows the status
jres=json.loads(response.text)
#print(jres)
result=jsonpath.jsonpath(jres,'message')
#print(result)
parameters = {
    "lat": 40.71,
    "lon": -74
}
#or
#urll="http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74."
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print(response.json())
