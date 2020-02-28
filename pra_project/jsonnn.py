import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"]) #30
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y) #{"name": "John", "age": 30, "city": "New York"}


print(json.dumps({"name": "John", "age": 30}))#{"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"])) #["apple", "bananas"]
print(json.dumps(("apple", "bananas"))) #["apple", "bananas"]
print(json.dumps("hello")) #"hello"
print(json.dumps(42)) #42
print(json.dumps(31.76)) #31.76
print(json.dumps(True)) #true
print(json.dumps(False)) #false
print(json.dumps(None)) #null






data={"name":"prabeena","marks":100,"address":["panda street","ballipadar",{"rank":1}]}
datas=json.dumps(data)#serialization
dat=json.loads(datas)#deserialization
if datas==dat:
  print("yes")
else:
  print("no") #no

print(type(datas)) #class "str"
print(type(dat)) #class "dict"
