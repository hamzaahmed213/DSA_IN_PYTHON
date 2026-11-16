# Given an integer array, find the element with the highest frequency and the element with the lowest frequency.

n = [1,1,2, 2, 2, 3, 3, 3, 4, 4, 5]

hash_dict = {}

for i in n:
    hash_dict[i] = hash_dict.get(i,0)+1

highest = float('-inf')
lowest = float('inf')

max_element = None
min_element = None

for k in hash_dict:
    if hash_dict[k] > highest:
        highest=hash_dict[k]
        max_element= k
    if hash_dict[k] < lowest:
        lowest=hash_dict[k]
        min_element = k

print("Highest frequency:", max_element, highest)
print("Lowest frequency:", min_element, lowest)

# T.C = O(NxK)
# S.C = O(K)