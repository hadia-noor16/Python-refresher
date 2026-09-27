# 2. Count word frequency
#    Given:
words = ["cat", "dog", "cat", "bird", "dog", "cat"]


# Create:
# {    "cat": 3,    "dog": 2,    "bird": 1}


# Then print the most frequent word.

dict={}

for word in words:
    if word not in dict:    # if word not in dict
        dict[word]=0      #  make its count 0
    dict[word]+=1        # else keep adding 1 for that word in dict
    
print(dict)

# Then print the most frequent word.

maximum=max(dict, key=dict.get)   #max(dict) would only get maximum from keys, and key=dict.get gets the value for each key.. max is taking max
print(maximum)
