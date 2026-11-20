# Given an integer N, print the word Coding exactly N times using recursion.

def func(n):
    if n==0:
        return
    print("Coding")
    func(n-1)

func(5)

# T.C = O(N)
# S.C = O(N) = STACK SPACE