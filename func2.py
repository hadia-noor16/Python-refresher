nums = [2, 7, 11, 15]
target = 9

#We need to return the indices of two numbers that add to 9.

def func (nums,target):
    n=len(nums)
    list=[]
    for i in range(n):
        for j in (i+1,n):
            if nums[i]+nums[j]==target:
                return[i,j]
                
    

list=func(nums,target)
print (list)