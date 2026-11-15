# Given two arrays, n and m, find how many times each element of m appears in n.

n = [1, 3, 2, 1, 3, 4, 2, 1]
m = [1, 2, 3, 4, 5, 6]

hash_list = [0] * (10**6)

for i in n:
    hash_list[i]+=1

for i in m:
    if 0 <= i < 10**6:
        print(f"{i} = {hash_list[i]}")

# T.C = O(NxM)
# S.C = O(10^6)
        
   
