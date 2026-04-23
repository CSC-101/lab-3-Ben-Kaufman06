def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and
                                           # the corresponding return value. n=1, n=2, n=3, n=4, which returns, 1, 4, 9, 16


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above? squares = [1, 4, 9, 16]. This matches the values recorded above because the list comprehension collects each return value from square(x).