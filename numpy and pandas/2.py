import numpy as np
a=np.array([[1,2,3],[2,3,4]],dtype=np.int) #set the type of array
b=np.zeros((2,3))
c=np.ones((5,5))
d=np.empty((2,2))
e=np.arange(10,20,2)
f=np.arange(12).reshape((3,4))
g=np.linspace(1,10,20).reshape((4,5)) #Return evenly spaced numbers over a specified interval.
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)