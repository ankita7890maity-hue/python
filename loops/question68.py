nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while i < len(nums):
    if nums[i] % 3 == 0:
        j = i + 1
        while j < len(nums) and nums[j] % 2 == 0:
            nums[j] *= 2
            j += 1
    i += 1
print(nums)