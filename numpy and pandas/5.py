import numpy as np
A=np.arange(3,15).reshape((3,4))
print(A)
print(A[1][1]) #same as next line
print(A[1,1])
print(A[2,:]) # 3rd row
print(A[:,1]) # 2nd column
print(A[1,1:3])
#print(A.flatten())
for row in A:
    print(row)
for column in A.T:
    print(column)
for item in A.flat:
    print(item)

B=np.arange(1,17).reshape((4,4))
C=B.T
print('C=\n',C)
