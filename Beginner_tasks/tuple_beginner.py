point = (3, 8)

# Print the first value.
# Print the second value.
# Unpack the tuple into x and y.
# Create a tuple with your name, age, and city.
# Try changing one tuple value and see what error you get.

print(f"first value: {point[0]}")

print(f" second value: {point[1]}")

print(point)

#Unpack the tuple
a,b=point
print(f" unpack 1st element: {a}")
print(f" unpack 2nd element: {b}")

new=("Hadia", "38", "Denver")

#new[0]= "Noor"

print(new)    # Error TypeError: 'tuple' object does not support item assignment

#Unpack values of new

x,y,z=new
print(y)