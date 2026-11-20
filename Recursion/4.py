# Given an integer N, calculate the sum of the first N natural numbers using recursion.

def func(n):
    if n ==0:
        return 0
    return n + func(n-1)
print(func(5))

