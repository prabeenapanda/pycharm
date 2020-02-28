def subString(s, n):
    # Pick starting point in outer loop
    # and lengths of different strings for
    # a given starting point
    for i in range(n):
        for len in range(i + 1, n + 1):
            print(s[i: len])

        # Driver program to test above function


s = "abcd"
subString(s, len(s))