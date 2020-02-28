#. Count consecutive characters say example i/p: aaabcdddd o/p: 3a1b1c4d
s=input("enter the input:")
i = 0
while (i < len(s) - 1):
    # Counting occurrences of s[i]
    count = 1
    while s[i] == s[i + 1]:
        i += 1
        count += 1
        if i + 1 == len(s):
            break
    print(str(s[i]) + str(count),end=" ")
    i += 1
print()

# Python3 code to demonstrate
# each occurrence frequency using
def fun():
    str=input("enter the input:")
    freq = {}
    for i in str:
        if i in freq:
             freq[i] += 1
        else:
             freq[i] = 1
    print(freq)
fun()
