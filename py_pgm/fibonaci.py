def fibonacci():
     limit = int(input("Give How many terms you want:"))
     i=0
     f = 0
     s = 1
     l=[]
     while (i < limit):
          if (i <= 1):
               Next = i
          else:
               Next = f + s
               f = s
               s = Next
          i = i + 1
          l.append(Next)
     print("The list of fibonacci series is:",l)
fibonacci()
