# Given a string, count how many times each lowercase English character appears.

s = "programming"

hash_list = [0] * 26

for letters in s:
    value = ord(letters)
    index = value-97
    hash_list[index] +=1

for i in range(26):
    if hash_list[i] != 0:
        print(f"{chr(i+97)}:{hash_list[i]}")

# T.C = O(Nx26)
# S.c = O(26)