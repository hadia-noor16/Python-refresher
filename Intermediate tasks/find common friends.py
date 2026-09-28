# 5. Find common friends
#    Given:

alice = {"Bob", "Sara", "John", "Mike"}
tom = {"Sara", "Mike", "Anna"}

# Find:
# - common friends
# - friends only Alice has
# - all unique friends between both
# This practices intersection, difference, and union.


common=(alice&tom)   #common friends   (intersection)
print(common)        # {'Mike', 'Sara'}

common=alice-tom      # friends only ALice has, so subtract friends of Tom . 
print(common)         # {Bob, john}

common=(alice|tom)    # union  (unique friedns between both) 
print(common)




