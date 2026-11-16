# Print only characters that appear more than once, along with their frequencies.

s = "mississippi"

hash_list = [0]*26

for letters in s:
    value = ord(letters)
    index = value - ord('a')
    hash_list[index]+=1

for i in range(26):
    if hash_list[i] > 1:
        print(f"{(chr(i + ord('a')))}->{hash_list[i]}")

# T.C = O(N+26)
# s.c = o(26)