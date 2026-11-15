# Find the number of divisors of a number

n = 10
from math import sqrt
count =0
for i in range(1, int(sqrt(n))+1):
    if n%i == 0:
        count +=1
    if n//i != i:
        count+=1

print(count)

# T.C = O(sqrt N)
# S.C = O(1)