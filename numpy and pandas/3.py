import numpy as np
from numpy.core.defchararray import count
a=np.array([10,20,30,40])
b=np.arange(4)
c=a**b #square
d=10*np.sin(a)
x=np.array([[1,2],[2,2]])
y=b.reshape((2,2))
z=x*y
z_dot=np.dot(x,y) #matirx times
print(a,b)
print(c)
print(d)
print(d<5)
print(x)
print(y)
print(z)
print(z_dot)