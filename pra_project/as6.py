#take a list print all non prime no from that using fun
a=[10,20,70,29,40,47,48,49,50,51,52,53]
for i in a:
    n=i
    def prime(p):
        c=0
        for i in range(2,p):
            if p%i==0:
                c=c+1
        if c==0:
            print(f'{p} is a Prime number')
        else:
            print(f'{p} is not a Prime number')
    prime(n)