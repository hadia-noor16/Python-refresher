set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


# Find:
# - union
# - intersection
# - values only in set1

print(f"union of sets: {set1 | set2}")   #union of sets: {1, 2, 3, 4, 5, 6}

print(f"Intersection of sets: {set1 & set2}")   #Intersection of sets: {3, 4}

# values that are in set1 but not in set2

print(set1-set2)      # {1,2}