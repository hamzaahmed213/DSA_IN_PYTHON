# Given an integer N, print all integers from 1 to N using recursion. You cannot use loops.

def func(n):
    if n==0:
        return
    func(n-1)
    print(n)

func(5)