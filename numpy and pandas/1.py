import numpy as np
from numpy.core.defchararray import array
array=np.array([[1,2,3],
               [2,3,4],
               [3,4,5],[2,2,2]]) #matrix setting
print(array)
print('number of dimention:',array.ndim) 
print('shape:',array.shape)
print('size:',array.size)
#How to calculate the reverse matrix
A=np.array([1,1,1,2]).reshape((2,2))
print(np.linalg.inv(A)) #can't be the singualr matrix
