from collections import Counter
words = ["api", "cloud", "api", "data", "cloud", "api", "data","cloud"]

# Given a list of words, return the most frequent word.
#If there’s a tie, return the word that comes first alphabetically.

def repeated_words (words):
    repeated={}
    for word in words:
        if word in repeated:
            repeated[word] +=1
        else:
            repeated[word] = 1
            
    print (repeated) #{'api': 3, 'cloud': 3, 'data': 2}
    
    max_count= max(repeated.values())
    candidates=[]

    for word in repeated:
        if repeated[word] == max_count:
            candidates.append(word)
        
 # Return alphabetically smallest
    return min(candidates)

print (repeated_words(words))   #prints api

        

#new=repeated(words)
# ma= dict(sorted(new.items(),key= lambda x:x[1]))  (prints in ascending order)
#print (new)  #{'api': 3, 'cloud': 3, 'data': 2}




        