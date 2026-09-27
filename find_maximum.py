nums = [3,7,2,9,4]

def max_num(nums):
    n=len(nums)
    for i in range(n):
        print(i)
        for j in range (0, n-i-1):
            if nums[j] >= nums[j+1]:
                nums[j], nums[j+1] = nums[j+1] , nums[j]
                
    return nums

print(max_num(nums))
print (nums[-1])
                