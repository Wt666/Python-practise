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
z_dot2=x.dot(y) #same as last line
print(a,b)
print(c)
print(d)
print(d<5)
print(x)
print(y)
print(z)
print(z_dot)
print(z_dot2)

a1=np.random.random((2,3)) #randomly get numbers
print(a1)
print(np.sum(a1)) #sum
print(np.min(a1))
print(np.max(a1))

print(np.sum(a1,axis=0)) #axis=0 means columns
print(np.min(a1,axis=1)) #axis=1 means rows