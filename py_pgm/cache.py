from functools import lru_cache
@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


fib={0:0,1:1}
def fibo(n):
     for i in range(2, n+1):
          fib[i]=fib[i-1]+fib[i-2]
     return(fib) #prints the series in dictionary
print(fibo(5))