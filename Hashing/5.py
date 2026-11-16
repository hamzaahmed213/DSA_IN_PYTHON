# Given a string containing uppercase, lowercase, digits and special characters, count the frequency of every distinct character.

s = "Hello@123Hello!!"

hash_dict = {}

for letters in s:
    hash_dict[letters] = hash_dict.get(letters,0)+1

print(hash_dict)

# T.C = O(N)
# S.C = O(k) K= distint character in dictionary

