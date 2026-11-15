# Question 1: Check whether a number is prime

n = 296

from math import sqrt
is_prime = True
for i in range(2, int(sqrt(n))+1):
    if n%i == 0:
        is_prime = False
        break
    

if is_prime:
    print("prime")
else:
    print("not")

# T.C = O(sqrt N)
# S.C = o(1)