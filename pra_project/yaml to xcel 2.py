import yaml
import re
import openpyxl as xl

with open("C:\\Users\\prabeena.panda\\Downloads\\cgs.yaml") as file:
    documents = yaml.full_load(file)
col = ["Group Name" , "Description", "Storage Location", "Storage","Priority"," Datastore",
       "|Vms","Replication","Server IP","Virtual Server Name"]
l=len(col)
Replication=[]
host_names=[]
list=documents["Virtual Server Name"]
servers=[]
host_names=[]
server_ip=[]
for i in list:
    servers.append(i.split(", "))
#print(servers)
for j in servers:
    for k in j:
         host_names.append(k.split(","))
#print(host_names)
result=[]
for m in host_names:
    for n in m:
    #print(m)
         result.append(n.split("__##__"))
#print(result)
host=[]
for l in result:
       #print(l)
       q = [x for x in l if not x.replace('.', '').isdigit() if not x.replace('.', '').isalpha()]
       host.append(str(q))
#print(host)
# res=[]
# for m in host_names:
#     for n in m:
#          res.append(n.split("__##__"))
#print(res)
for p in result:
        q=[x for x in p if x.replace('.','').isdigit()]
        server_ip.append(str(q))
print(server_ip)
print(host)
# documents["Server IP"]=server_ip
# documents["Virtual Server Name"]=host
#
# #print(documents)
# for doc in documents.values():
#         Replication.append(doc)
# target_file = "c:\\Users\\prabeena.panda\\targe.xlsx"
# Owb= xl.load_workbook(target_file)
# Ows = Owb.worksheets[0]
# for row_num, row in enumerate(Replication):
#     #print(row_num,row)
#     for col_num , value in enumerate(row):
#         #print(col_num,value)
#          Ows.cell(row=col_num+3, column=row_num+1).value = value
# Owb.save(target_file)