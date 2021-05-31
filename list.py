#tuple list
a_tuple=(1,2,3)
another_tuple=1,2,3,4
a_list=[1,2,34,4,4,4,4,4,4,66]
#for i in a_list:
#   print(i)
for index in range(len(a_list)):
    #range(5)
    print('index=',index,'number in list=',a_list[index])
print(a_list[1])

a=[1,2,3,4,5,6,7,8]
print(a[2])
print(a[-1])
print(a[0:2]) #From 0th to 2nd (not include 2nd)
print(a[3:5]) #From 3rd to 5th (not include 5th)
print(a[-3:])
print(a.index(2))
print(a.count(2))

a.append(0)
a.insert(1,9)
a.insert(0,10)
#a.remove(3)
print(a)
print(a[2])
print(a[-1])

b=[1,2,4,6,7,2,23,4,6]
b.sort(reverse=True)
print(b)