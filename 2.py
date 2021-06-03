import numpy as np
from functools import reduce
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)
multiply(1,2,3,4,5,6,7)
def sum():
    sum=0
    for i in range(0,101):
    
        sum = sum+i
    return sum
print(sum())

def a(x,y):
    return x+y
print(reduce(a,range(0,101)))
print(reduce((lambda x,y:x+y,range(0,101))))
