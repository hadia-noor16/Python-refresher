words = {
    2: ["an", "go", "be"],
    3: ["cat", "dog"],
    4: ["book", "tree"]
}

# Tasks:
# - Print all 3-letter words.
# - Add "sun" to the 3-letter list.
# - Print how many 4-letter words there are.
# - Loop through the dictionary and print:
# 2 -> ['an', 'go', 'be']
# 3 -> ['cat', 'dog', 'sun']
# 4 -> ['book', 'tree']


three_letter=(words[3])    # words with key=3
print(three_letter)        # ['cat', 'dog']

words[3].append("sun")     # output {2: ['an', 'go', 'be'], 3: ['cat', 'dog', 'sun'], 4: ['book', 'tree']}
print(words)      

if words[4]:                # this only works if key 4 exists in dictionary
    four_letter=len(words[4])
print(four_letter)   

# if key=4 doesn't exist in dict, we should handle taht case to..hence

four_letter= len(words.get(4, []))   # if 4 exist as key, bring it, otherwise return empty list, and len(empty)==0
print(four_letter)        

for key,value in words.items():
    print(f" {key} -> {value}")