# 8. Function challenge: second largest
#    Write:
# def second_largest(numbers):

# It should return the second largest unique number.
# Example:
# second_largest([10, 5, 8, 10, 7])

# should return:
# 8


def second_largest(numbers):
    unique_numbers=list(set(numbers))         # removes duplicate from lists using "set", and retuen a list, if you don't retrun a list, sort will fail
    print(unique_numbers)  
    unique_numbers.sort(reverse=True)    # sort the list in desc order
    return(unique_numbers[1])            # return second highest number
print(second_largest([10, 5, 8, 10, 7]))