import yaml
import openpyxl as xl

with open("C:\\Users\\prabeena.panda\\Downloads\\cgs.yaml") as file:
    documents = yaml.full_load(file)
    #print(documents)

    #for item, doc in documents.items():
        #print(item, "->", doc)

#col = ["Group Name" , "Description", "Storage Location", "Storage","Priority"," Datastore","|Vms","Replication",
       #"Server IP","Virtual Server name"]
Replication=[]
for doc in documents.values():
        Replication.append(doc)
#print(Replication)
target_file = "c:\\Users\\prabeena.panda\\targe.xlsx"
Owb= xl.load_workbook(target_file)
Ows = Owb.worksheets[0]
for row_num, row in enumerate(Replication):
    #print(row_num,row)
    for col_num , value in enumerate(row):
        #print(col_num,value)
         Ows.cell(row=col_num+3, column=row_num+1).value = value
Owb.save(target_file)