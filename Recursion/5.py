# Given a non-negative integer N, calculate its factorial using recursion.

def func(n):
    if n == 1:
        return 1
    return n * func(n-1)

print(func(5))