data={"name":"gss","clients":[{"name":"sungard","teams":[{"name":"netsec","size":10},{"name":"aws","size":20}]}]}
print(data["name"])
print(data["clients"])
print(data["clients"][0]["name"])
print(data["clients"][0]["teams"])
print(data["clients"][0]["teams"][0]["name"])
print(data["clients"][0]["teams"][0]["size"])
print(data["clients"][0]["teams"][1]["name"])
print(data["clients"][0]["teams"][1]["size"])


for c in data["clients"]:
    print(c)
    if c["name"] == "sungard":
        print(c["teams"])
        print({x["name"] for x in c["teams"]})
        print(sum({x["size"] for x in c["teams"]}))
        print({x["size"] for x in c["teams"] if x["name"] == "aws"})



d={"name":"gss","clients":{"name":"sungard","teams":[{"name":"netsec","size":10},{"name":"aws","size":20}]}}
for c in d["clients"]:
     #print({x["name"] for x in c["teams"]})
     #print(c.values())
