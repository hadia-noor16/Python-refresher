
def sum(x):
    x=[1,2,3,4,5,6,7,8]
    if length (x)==1:
        return x[0]
    
    else:
        midpoint = floor(length(x)/2)
        
    
    return sum(x[0:midpoint]) + sum (x[midpoint:length(x)])

x=[1,2,3,4,5,6,7,8]
r=sum(x)
print (r)