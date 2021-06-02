import numpy as np
A=np.arange(3,15).reshape((3,4))
print(A)
print(A[1][1]) #same as next line
print(A[1,1])
print(A[2,:]) #2nd row
print(A[:,1]) #1st column
print(A[1,1:3])
#print(A.flatten())
for row in A:
    print(row)
for column in A.T:
    print(column)
for item in A.flat:
    print(item)