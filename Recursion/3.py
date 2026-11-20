# Given an integer N, print all integers from N down to 1 using recursion.

def func(i,n):
    if i == 0:
        return
    print(i)
    
    func(i-1,n-1)

n = 5
i = n
func(i,n)

# T.C = O(N)
# S.C = O(N) = STACK SPACE