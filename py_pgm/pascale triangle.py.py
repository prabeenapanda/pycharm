#Write a Python function that that prints out the first n rows of Pascal's triangle.
def pascal(n):
   row = [1]
   y = [0]
   for x in range(max(n,0)):
      print(row)
      row=[l+r for l,r in zip(row+y, y+row)]
   return n>=1
pascal(6)

#normal triangle
def printPascal(n):
   for r in range(1, n + 1):
      v = 1
      for i in range(1, r + 1):
         print(v, end=" ")
         v = int(v * (r - i) / i)
      print("")
n = 6
printPascal(n)
