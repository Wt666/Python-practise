#print("I'm\" apple")
#print("apple"+"4")
#print("1.2+2")
#print(int("1")+2)
#print(float("1.2")+3)
# print(a)
# i=int(input("Enter the number:"))
# if (i<=10):
#     print("i is less than 10")
# else:
#     print("i is larger than 10")

# num = int(input("Enter the number:")) 
# if (num % 2== 0):
#     print ("Given number is Even") 
# else: 
#     print("Given number is Odd")

# a=int(input())
# if a<60:
#     print("not pass")
# elif 60<=a<=80:
#     print("liang")
# elif 80<a<=90:
#     print("good")
# else:
#     print("very good")

# n=int(input("Enter number:"))
# if n<=15:
#     if n==10:
#         print("play cricket")
#     elif n==8:
#         print("play ow")
#     else:
#         print("play kabadi")
# else:
#     print("Don't play game")

# import random
# x=random.choice(range(100))
# y=random.choice(range(200))
# if x >y:
#     print("x="+x)
# elif x==y:
#     print(str(x)+str(y))
# else:
#     print("y="+y)
# a=int(input("Enter a number:"))
# sum=0
# while a>0:
#     sum=sum+a
#     a=a-1
# print(sum)

# b=0
# sum1=0
# while b<=100:
#     sum1=sum1+b
#     b=b+1
# print(sum1)

# counter=0
# while counter<3:
#     print("inside loop")
#     counter=counter+1
# else:
#     print("outside loop")
# import matplotlib.pyplot as plt

# a=[1,2,3]
# b=[i*2 for i in a]
# # print(b)
# plt.plot(a,b)
# plt.show()
numbers=[1,2,3,4,5324,324,324,234]
sum=0
for i in numbers:
    sum=sum+i
print(sum)

a=int(input("Enter a number:"))
sum=0
while a>0:
    sum=sum+a
    a=a-1
print(sum)
