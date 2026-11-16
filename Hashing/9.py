# Given a string, find the first character that appears exactly once.

s = "aabbcdeeff"
st = s

hash_list = [0]*26

for i in st:
    value = ord(i)
    index = value - ord('a')
    hash_list[index] +=1

for i in s:
    index = ord(i) - ord('a')


    if hash_list[index] == 1:
        print(i)
        break

# T.C = O(N+26)
# S.C= O(26)