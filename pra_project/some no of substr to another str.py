str=input("enter the string:")
sub=input("enter the substr:")
l=str.split(" ")
print(l)
st=" "
n=int(input("enter the number of substr u want to change:"))
for i in range(0,n):
    l[i]=sub

print(st.join(l))
