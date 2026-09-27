# Question: Count how many even numbers are in:

nums = [1,2,3,4,5,6]

def even_nums(nums):
    count=0
    for i in nums:
        #print (i)
        if i % 2==0:
           #print (nums[i])
           count+=1
            
    return count

count=even_nums(nums)
print (count)

# Clear one line answer
count = len([x for x in nums if x % 2 == 0])