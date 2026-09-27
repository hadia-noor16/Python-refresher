nums = [1, 2, 3, 5]
actual_sum=sum(nums)
#print(actual_sum)

#One number from 1 to 5 is missing.

#Return the missing number.

# 4 is missing from the list, so according to math formula n=5 (beacuse list should have 5 numbers)

# Expected sum == > n(n+1)/2 == 5*6/2 == 15
# Actual sum ==> 11 (5+3+2+1)

# missing number = expected sum- actual sum i.e. 4

def missing_num(nums,actual_sum):
    n=len(nums)+1
    expected_sum= (n*(n+1))//2
   # print(expected_sum)   
    return expected_sum - actual_sum

number=missing_num(nums,actual_sum)
print(number)      