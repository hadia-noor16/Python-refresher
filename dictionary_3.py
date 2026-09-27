person = {
    "name": "Hadia",
    "age": 25,
    "city": "Austin"
}
print(person)   #print whole dict as is
print(person["city"])   #prints Austin

# add or update value
 
person["age"] = 38   # changes age to 38
#print (person.items())  #prints all dictionary item as list

for item in person:
    print (item,person[item])  #List all key values of dict
    
for key,value in person.items(): #List all key values of dicts
    print(key,value)
    
    
#Nested dictionary
students = {
    "A": {"math": 90, "science": 85},
    "B": {"math": 80, "science": 88}
}

print (students["A"]["math"])   #prints 90


# Sort dictionary by value
d = {"a":3, "b":1, "c":2}
sorted_d = dict(sorted(d.items(), key=lambda x:x[1]))
print (sorted_d)   # prints {'b': 1, 'c': 2, 'a': 3}


# comprehension
nums = [1,2,3,4]
squares = {x:x*x for x in nums}
print(squares)

person.pop("age")  # will remove item age from dict
print (person)   #{'name': 'Hadia', 'city': 'Austin'}