#.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.def string_test(s):
def test(s):
    UPPER=0
    LOWER=0
    for c in s:
        if c.isupper():
           UPPER+=1
        elif c.islower():
           LOWER+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ",UPPER)
    print ("No. of Lower case Characters : ",LOWER)
test('My Name Is Prabeena')
