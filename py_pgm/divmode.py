#divmod(x, y)
#x and y : x is numerator and y is denominator
#x and y must be non complex
#If x and y are integers, the return value is
#(x / y, x % y)



print('(5, 4) = ', divmod(5, 4))
print('(10, 16) = ', divmod(10, 16))
print('(11, 11) = ', divmod(11, 11))
print('(15, 13) = ', divmod(15, 13))
# divmod() with int and Floats
print('(6.0, 5) = ', divmod(8.0, 3))
print('(3, 9.0) = ', divmod(3, 8.0))
print('(13.5, 6.2) = ', divmod(7.5, 2.5))
print('(1.6, 10.7) = ', divmod(2.6, 0.5))


#prime number
n = 15
x = n
count = 0
while x != 0:
    p, q = divmod(n, x)
    x -= 1
    if q == 0:
        count += 1
if count > 2:
    print('Not Prime')
else:
    print('Prime')


# Sum of digits of a number using divmod
num = 86
sums = 0
while num!=0:
    use = divmod(num, 10)
    dig = use[1]
    sums = sums + dig
    num = use[0]
print(sums)



# reversing a number using divmod
num = 132
pal = 0
while num!=0:
    use = divmod(num, 10)
    dig = use[1]
    pal = pal*10+dig
    num = use[0]
print(pal)