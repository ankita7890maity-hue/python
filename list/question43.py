nums=[5,3,8,1,9]
temp=nums[2]
nums[2]=nums[0]
nums[0]=temp
print(nums)
print(max(nums))
print(min(nums))
