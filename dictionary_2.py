# Write Python code to count how many times each character appears in:

text = "data"

#Expected output:

#{'d':1, 'a':2, 't':1}

def char_count(text):
    counts={}
    for c in text:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            
    return counts

print (char_count(text))
            
            