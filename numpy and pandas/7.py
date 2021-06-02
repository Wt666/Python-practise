import numpy as np
A=np.arange(12).reshape((3,4))
print(A)
print(np.split(A,2,1))
print(np.split(A,3,0))
print(np.array_split(A,3,1)) #no equal split
print(np.vsplit(A,3)) #vertical split
print(np.hsplit(A,2)) #horizontal split