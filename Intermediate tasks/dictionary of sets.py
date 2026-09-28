# 7. Dictionary of sets
#    Given friendships:
pairs = [    ("Ali", "Sara"),    ("Ali", "John"),    ("Sara", "Maya"),    ("John", "Maya")]

# Build:
# {    "Ali": {"Sara", "John"},    "Sara": {"Ali", "Maya"},    "John": {"Ali", "Maya"},    "Maya": {"Sara", "John"}}

# The input is list of tuples
# the output is dictionary of set
# sets do not preserve a predictable order when printed.

dict={}
for p,pair in pairs:
    if p not in dict:
        dict[p]= set()
    if pair not in dict:
        dict[pair]= set()
    
    dict[p].add(pair)
    dict[pair].add(p)   # sets do not preserve a predictable order when printed. so values could be in any order
    
print(dict)
        
