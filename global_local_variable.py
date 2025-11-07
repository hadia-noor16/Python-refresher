num = 10

def number():
    num=5  #local variable
    return (int(input("Enter a  number : "))) *num   #num is 5 now, variable inside function takes precedence.

result=number()
print(result)   #output = 25, input=5

print(num)  # outside of fucntion  num=10


#If you don't want to change the value of num in side any function and fear of overwritten, 
# declare numas global varibale inside the function

num = 10

def number():
    global num  # num is now defined as global variable 
    return (int(input("Enter a  number : "))) *num   #num stays 10 now, so (x * 10), variable inside function takes precedence.

result=number()
print(result)   #output = 50, input=5 