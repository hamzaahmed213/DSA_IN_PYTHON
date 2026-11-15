# Factors of a number

from math import sqrt
num = 20
factor=[]
for i in range(1, int(sqrt(num))+1):
    if num%i == 0:
        factor.append(i)
    if num//10 != 0:
        factor.append(num//i)


print(factor)

# T.C = O(sqrt N)
# S.C = O(K)