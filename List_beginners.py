numbers = [4, 7, 2, 9, 7, 1]

# #tasks
# Print the first item.
# Print the last item.
# Add 5 to the list.
# Remove 2.
# Count how many times 7 appears.
# Sort the list.
# Find the largest and smallest number.

print( f"first item:  {numbers[0]}")
print(f" last item: {numbers[-1]}")
numbers.append(5)
print(f" append 5: {numbers}")
numbers.pop(2)
print(f" remove 2 : {numbers}")

count=0
for num in numbers:
    if num==7:
        count+=1
print(f" 7 appears {count} times")

numbers.sort()
print(f"sort the list: {numbers}")

numbers.sort(key= lambda x : x)
print(f"smallest number : {numbers[0]}")
numbers.sort(key= lambda x:x, reverse=True)
print(f" Largest number: {numbers[0]}")