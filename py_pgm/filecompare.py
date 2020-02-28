file1 = open('some_file_1.txt', 'r')
file2 = open('some_file_2.txt', 'r')
FO = open('some_output_file.txt', 'w')

for line1 in file1:#By looping through the lines of the file,
    # you can read the whole file, line by line:
    for line2 in file2:
        if line1 == line2:
            FO.write("%s\n" %(line1))

FO.close()
file1.close()
file2.close()
f=open("file1",'a')
f.write("Now the file has more content!")#add this line to the file but open it in append mode
                                         # if u open in write it will delete the previous content
g=open("file2",'r')
for l1 in f:
    for l2 in g:
        if l1==l2:
           print("matched")
        else:
            print("not matched")
f.close()
g.close()
