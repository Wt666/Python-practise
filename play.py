x=int(input("the first number you input"))
y=int(input("the second number you input"))
def add(x,y):
    sum=0
    for i in range(x,y+1):
        sum=sum+i
    return sum
print(add(x,y))