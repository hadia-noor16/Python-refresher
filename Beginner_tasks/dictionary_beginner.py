student = {
    "name": "Sara",
    "age": 20,
    "grade": 91
}

# Tasks:
# - Print the student's name.
# - Change the grade to 95.
# - Add "city": "Denver".
# - Print all keys.
# - Print all values.
# - Loop through both keys and values.

print(f" student name: {student["name"]}")

student["grade"] = 95

print(f"change grade to 95 : {student["grade"]}")

# add city Denver

student["city"] = "Denver"    # added key=city, Value= Denver
print(student)

for key in student:
    print(key)         #only keys

for value in student.values():
    print(value)                  # only values

# - Loop through both keys and values.

for key,value in student.items():    #both
    print(f" {key}: {value}")