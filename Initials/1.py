#count the numbers in a digit

n = 14323
num = n
count =0
while num > 0:
    last_digit = num%10
    count+=1
    num = num//10
print(count)

# T.C = O(Log10 N)
# S.C = O(1)

