# Given an array n, count how many times each number appears
n = [1, 2, 3, 2, 1, 4, 5, 2, 3, 1]

hash_list =[0]*11 

for i in n:
    hash_list[i]+=1

for i in range(0,10):
    if hash_list[i] != 0:
        print(f"{i} -> {hash_list[i]}")

# T.C = O(N+10)
# S.C = O(11)