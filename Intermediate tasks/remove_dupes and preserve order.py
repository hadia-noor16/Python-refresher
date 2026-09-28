# 4. Remove duplicates but preserve order
#    Given:
numbers = [4, 2, 4, 7, 2, 8, 7, 1]

# Produce:
# [4, 2, 7, 8, 1]

# Do not just use:
#     set(numbers)

nums=[]
for num in numbers:
    if num not in nums:
        nums.append(num)
    
print(nums)             # the output is fine, but for longer list it takes O(n^2)

# To make it faster, use below code

nums=[]
seen=set()
for num in numbers:
    if num not in seen:
        seen.add(num)
        nums.append(num) 
        
print(nums)       