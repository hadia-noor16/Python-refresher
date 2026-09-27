words = ["apple", "ant", "banana", "boat", "cat", "car", "dog"]

# Group words by first letter

# {
#     "a": ["apple", "ant"],
#     "b": ["banana", "boat"],
#     "c": ["cat", "car"],
#     "d": ["dog"]
# }

dict={}
for word in words:
    i=word[0]    # assign i as first letter of word
    if i not in dict:     # check if i is already existing key in dict
        dict[i] = []      # if not, set an empty list as its value
    dict[i].append(word)  # because value(word) is a list, so we used append fucntion
print(dict)