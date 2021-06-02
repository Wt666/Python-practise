import numpy as np
from numpy.lib.index_tricks import AxisConcatenator
A=np.arange(2,14).reshape((3,4))
print(np.argmin(A))
print(np.argmax(A))
print(np.mean(A)) #same as next line
print(A.mean())
print(np.median(A))
print(np.cumsum(A))
print(np.diff(A))
print(np.nonzero(A))
print(np.sort(A))
print(np.transpose(A))#same as next line
print(A.T)
print((A.T).dot(A))
print(np.clip(A,5,9))#less than 5 is 5 & larger than 9 is 9
print(np.mean(A,axis=1))#row
print(np.max(A,axis=0))