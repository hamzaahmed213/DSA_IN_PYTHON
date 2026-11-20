# Given a string, reverse only the vowels in the string. All consonants must remain in their original positions.
s="leetcode"

def func(s,l,r):
    
    if l>r:
        return s
    if s[l].lower() not in "aeiou":
        return func(s,l+1,r)
    if s[r].lower() not in "aeiou":
        return func(s,l,r-1)

    s[l],s[r] = s[r],s[l]

    return func(s,l+1,r-1)    

s= list(s)
l=0
r=len(s)-1
answer = func(s,l,r)
print("".join(answer))
