usernames = {
    "hadia": "hadia123",
    "noor" : "noor_1",
    "musab": "Musab_A",
    "fatima" : "Fatima1"
}

for key in usernames:
    print(key)    # prints only key
    print (usernames[key])   # print values only
   
    print(key,"," ,usernames[key])  # prints key and values both
    
print(usernames.items())   # prints dictionary ([('hadia', 'hadia123'), ('noor', 'noor_1'), ('musab', 'Musab_A'), ('fatima', 'Fatima1')])


#modifying value of a key
usernames["hadia"] = "hadianoor"
print (usernames)   # output {'hadia': 'hadianoor', 'noor': 'noor_1', 'musab': 'Musab_A', 'fatima': 'Fatima1'}

#deleting items
del usernames["fatima"]
print (usernames)    # deleted Fatima as username

#remove last  item from dictionary
usernames.popitem()

#remove all items from dictionary
usernames.clear()
