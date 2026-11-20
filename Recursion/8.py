# Given a string, reverse it by swapping characters from opposite ends. You must use recursion and cannot use loops or built-in reverse functions.

s = "programming"

def func(s,l,r):
    if l>r:
        return s
    s[l], s[r] = s[r], s[l]
    return func(s,l+1,r-1)

l = 0
r = len(s)-1
s = list(s)
answer = (func(s,l,r))
print("".join(answer))