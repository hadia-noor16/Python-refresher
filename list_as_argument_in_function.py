def multiply_values(list):
    multiplied_values = []
    for item in list:
        multiplied_values.append(item * 2)
    return multiplied_values

new_list=multiply_values([2,3,4])
print(new_list)