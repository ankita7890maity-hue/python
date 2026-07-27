nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        j = i + 1
        count = 0
        while j < len(nums) and count < 2:
            if nums[j] % 2 == 1:
                result.append(nums[j])
                count += 1
            j += 1
    i += 1
print(result)