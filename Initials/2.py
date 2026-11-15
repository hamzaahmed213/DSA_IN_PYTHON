#check if a number is palindrome or not

n = 1234
num = n
temp = 0

while num >0:
    last_digit = num%10
    temp = temp*10 + last_digit
    num = num//10

if temp ==n:
    print("palindrome")
else:
    print("not")

# T.C = O(Log 10 N)
# S.C = O(1)