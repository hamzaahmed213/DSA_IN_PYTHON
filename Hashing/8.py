# Find the common elements between two arrays. Print each common element only once, along with its frequency in the first array.

n = [1, 2, 3, 4, 5, 2, 3]
m = [2, 3, 6, 7, 2, 8]

hash_dic = {}

for i in n:
        hash_dic[i] = hash_dic.get(i,0)+1

seen = set()

for i in m:
    if i in hash_dic and i not in seen:
        print(f"{i} is common, frequency: {hash_dic[i]}")
        seen.add(i)

        
# T.C = O(NxM)
# S.C = O(K)