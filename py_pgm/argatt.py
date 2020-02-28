
#argument attribute
class Addition:
    def add(self,num1,*args):
        if num1 is int:
            print(num1," INT")
        else:
            print(num1)
        for i in args:
            print(i)
    def addit(self,**kwargs):
        for key,value in kwargs.items():
            print(key," ",value)
ad = Addition()
ad.add(10)
ad.add("MAD",1,2,3,4)
ad.addit(x="1",y="2")
kwargs={'1':'10','2':'20','3':'30'}
ad.addit(**kwargs)