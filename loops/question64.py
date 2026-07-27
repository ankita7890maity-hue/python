# Guess the output of the following code:
nums = [1, 2, 3, 4, 5]
i = 0
while i < len(nums):
    if nums[i] > 3:
        nums = nums[:i] + nums[i+1:]
        continue
    i += 1
print(nums)