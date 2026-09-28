# 6. Sort tuples by multiple rules
#    Given:
students = [    ("Ali", 90),    ("Sara", 95),    ("John", 90),    ("Maya", 88)]

# Sort by:
# - score descending
# - if tied, name alphabetically ascending
# Expected:
# [    ("Sara", 95),    ("Ali", 90),    ("John", 90),    ("Maya", 88)]

# list of tuples

students.sort(key=lambda x: (-x[1] , x[0]))    #sort desc means -x[1], because marks in at 1 index,
print(students)                                # and if tie in marks, sort x[0], so sort by name thats at index 0
