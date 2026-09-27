words = ["cat", "dog", "apple", "go", "tree", "an", "house"]

# Create a dictionary that groups words by length.
# Expected idea:
# {    2: ["go", "an"],    3: ["cat", "dog"],    4: ["tree"],    5: ["apple", "house"]}

dict={}
for word in words:  # for each word in dict
    w=len(word)     # assign its length to w
    if w not in dict:    # look if w (key) already in dict
        dict[w]=[]       # if not, set an empty list as its value
    dict[w].append(word)    # otherwise if key already exists, append the word to the list for its length
print(dict)
    