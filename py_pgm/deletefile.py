import os
#rename file
os.rename( "test1.txt", "test2.txt" )
#delete file
os.remove("demofile.txt")
#to check if file exist or not
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
#delete folder
os.rmdir("myfolder")