nums = [5, 2, 8, 1, 9]
target = 8
index = nums.index(target)
nums[index] = nums[0]
nums[0] = target
print(nums)
print(nums.index(5))