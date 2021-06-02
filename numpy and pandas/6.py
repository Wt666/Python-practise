import numpy as np
A=np.array([1,1,1])#[:,np.newaxis]
B=np.array([2,2,2])#[:,np.newaxis]
print(np.vstack((A,B))) #vertical stack
print(np.hstack((A,B))) #horizontal stack
print(A.shape)
print(A[:,np.newaxis]) # change the dimension of A
print(A[:,np.newaxis].shape) #the shape of line 7

C=np.concatenate((A,B),axis=0) #multi array 
print(C)