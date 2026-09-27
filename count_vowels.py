string= "datascience"

def count_vowels(string):
    count=0
    vowels = ['a','e','i','o','u']
    for word in string:
        if word in vowels:
            count+=1
            
    return count

print(count_vowels (string))