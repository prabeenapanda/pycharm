# **kwargs is for strings we can pass string as value here in cotation and
# args is for integer we cannt pass value using any other value we have to pass the exact value.


from itertools import cycle
class testcode():
    def testcode(self,**kwargs):
        try:
            day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            pool = cycle(day)
            print(day)
            sum = 0
            for i in day:
                if i==kwargs['string']:
                    sum = day.index(i)
            sum += int(kwargs['n'])
            for i,j in enumerate(pool):
                if i==sum:
                    return j
        except IndexError:
            print("Error occured, please check the code")