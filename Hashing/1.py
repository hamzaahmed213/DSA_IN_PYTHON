#find if elements of n are in m with constraint 1<= n[i] =>10

n = [1,3,6,2,1,4,6,7,10,2,4,6]
m=[1,32,2,4,5,34,23,2,6,10,11,67]

hash_list = [0] * 11

for nums in n:
    hash_list[nums] +=1

for nums in m:
    if nums < 1 or nums >10:
        continue
    else:
        print(hash_list[nums])