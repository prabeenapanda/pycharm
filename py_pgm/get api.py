import requests
url="http://api.open-notify.org/astros.json"
response=requests.get(url)
print(response)
print(response.status_code)
