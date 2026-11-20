# Given an array of integers, reverse the array using recursion without using loops.

nums = [1, 2, 3, 4, 5]

def func(nums,l,r):
    if l > r or l == r:
        return nums
    nums[l],nums[r] = nums[r],nums[l]
    return func(nums, l+1, r-1)

l = 0
r = len(nums)-1
print(func(nums,l,r))

# T.C = O(N)
# S.C = O(N) = STACK SPACE