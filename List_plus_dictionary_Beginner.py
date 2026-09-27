students = {
    "Ali": 85,
    "Sara": 92,
    "John": 78
}

# Tasks:
# - Print Sara's score.
# - Add "Maya": 88.
# - Find the student with the highest score.
# - Print only students who scored above 80.

print(f" Sara's score: {students["Sara"]}")

# Add maya score
students["Maya"] = 88
print(students)

# - Find the student with the highest score.

# max=max(students.values())
# print (max)

# for key,value in students.items():
#     if value == max:
#         print(key)

#OR SHORTER VERSION IS

top_student= max(students, key=students.get)   #If you do max(students) it will only sort with keys
print(top_student)                             # key=students.get actually get the value of that key 

# print only student who scored above 80

for key,value in students.items():
    if value>80:
        print(key)