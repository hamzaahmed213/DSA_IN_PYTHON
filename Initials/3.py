# ARMSTRONG'S NUMBER
# 153 = 1^3 + 5^3 + 3^3
n = 153
lod = len(str(n))
num = n
total = 0

while num >0:
    last_digit = num%10
    total = total + (last_digit ** lod)
    num = num//10

if total == n:
    print("Armstrong")
else:
    print("not")
    
# T.C = O(Log10 N)
# S.C = O(1) auxilary space
