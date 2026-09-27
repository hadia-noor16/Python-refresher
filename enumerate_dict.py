nums = [2,7,11,15]
seen = {}

for i, num in enumerate(nums):
    if num not in seen:
        seen[num] = i

print(seen)