a=[1,2,3]
b=[4,5,6]
zip(a,b)
print(list(zip(a,b)))
for i,j in zip(a,b):
    print(i/2,j*2)
print(list(zip(a,a,b)))

def fun1(x,y):
    return x+y
fun1(1,2)

fun2=lambda x,y: x+y
print(fun2(2,3))

print(list(map(fun1,[1,3],[3,3])))

def square(x):
    return x**2

print(list(map(square,[1,2,3,4,5,6])))


