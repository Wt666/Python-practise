import copy
a=[1,2,3,4]
b=a #all equal
b[0]=11
a[1]=22
print(id(a)==id(b))

c=copy.copy(a) #shallow copy: just copy first layer
print(c)
e=copy.deepcopy(a) #deep copy: 
print(e)
