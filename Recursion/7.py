# Given a string S, determine whether it is a palindrome using recursion.

s = "madam"
h = "hamza"

def func(s,l,r):
    if l>r:
        return True
    if s[l] != s[r]:
        return False

    return func(s,l+1,r-1)

r = len(s)-1
l =0
print(func(s,l,r))