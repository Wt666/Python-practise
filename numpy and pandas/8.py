import numpy as np
a=np.arange(4)
print(a)
b=a
c=a
d=b
a[0]=11
print(b)
print(b is a) #ture
print(d is a)
d[1:3]=[22,33]
print(d)
e=a.copy() # shallow copy
print('e=',e)
a[0]=9999
print('now a=',a)
print('now e=',e)