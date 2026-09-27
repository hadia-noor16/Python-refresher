fruits = {"apple", "banana", "orange", "apple"}

# Tasks:
# - Print the set and notice what happens to duplicate "apple".
# - Add "grape".
# - Remove "banana".
# - Check whether "orange" is in the set.
# - Find the length of the set.

print(f" print set: {fruits}")   #apple is removed because appearing twice, set remove dupes

fruits.add("grape")
print("Add grape" ,fruits)   #Add grape {'apple', 'banana', 'orange', 'grape'}

fruits.remove("banana")
print("Remove Banana", fruits)  #Remove Banana {'apple', 'grape', 'orange'}

# Two ways to write if orange exist in set
print({x for x in fruits if x=="orange"})   # {'orange'}

print("orange" in fruits)                   # True

# Length of the set
print(len(fruits))                        # 3 , because set only keeps unique values

# sort fruits by names

#fruits.sort()   #set cannot be sorted in-place like a list

print(sorted(fruits))      #Sorted return a list, not a set           # ['apple', 'grape', 'orange']

