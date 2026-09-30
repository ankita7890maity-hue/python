nums=[1,2,3,45]
even_positive=nums[::2]
odd_positive=nums[1::2]
combined=even_positive+odd_positive
print(len(combined))
print(combined[-1])
