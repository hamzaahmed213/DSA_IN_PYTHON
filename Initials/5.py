num = [1,5,8,2,5,6,1,3,9,5,6,9,7,2,1,3,6,4]

lenght = len(num)
freq ={}

for i in range(0,lenght):
    freq[num[i]] = freq.get(num[i],0)+1

print(freq)

# T.C = O(N)
# S.C = O(N)