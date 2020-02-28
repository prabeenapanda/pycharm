#Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
def findTriplets(arr):
    n = len(arr)
    found = True
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
    if (found != True):
        print(" not exist ")
arr = [0, -1, 2, -3, 1]
findTriplets(arr)