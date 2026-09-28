# 3. Students and averages
#    Given:
students = {    "Ali": [80, 90, 85],    "Sara": [95, 92, 88],    "John": [70, 75, 72]}

# Create a new dictionary containing each student’s average.
# Expected idea:
#     {
#     "Ali": 85.0,
#     "Sara": 91.67,
#     "John": 72.33
# }
#     Then find the student with the highest average.

dict={}
#print(type(score))
for student,marks in students.items():
    score=0
    for mark in marks:
        #print(type(mark))
        score+=mark
    avg=round(int(score)/len(marks),2)   # use round(avg, 2) to 2 digits after float
    
    dict[student]=avg
print(dict)                            #{'Ali': 85.0, 'Sara': 91.67, 'John': 72.33}

maximum=max(dict, key=dict.get)
print(maximum)
    
    
    