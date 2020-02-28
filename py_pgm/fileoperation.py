f1=open("file1.txt",'w+')
for i in range(10):#to create a file
     f1.write("This is line %d\r\n" % (i+1))
print(f1.read())#read the whole file and print
print(f1.read(5))#first 5 char
print(f1.readline())#read nd print a line
print("name of the file:",f1.name)
print("closed or not:",f1.closed)
print("mode of the file",f1.mode)
#print("softspace flag:",f1.softspace)
fo = open("file1.txt", "r+")
str = fo.read(100)
print ("Read String is : ", str)
position = fo.tell()
print ("Current file position:",position)#106 100 letter  nd 6 \n
#pos = fo.seek(0, 2)#171 coz there will be total that many lines
#pos= fo.seek(0,0)#0 coz it will be at first position only
#pos= fo.seek(0,1)#106 coz it go till the current position before
pos=fo.seek(9,5)#in(offset,from) the offset must be 0 and from must be in 0,1,2
print ("Current file position:",pos)
f1.close()