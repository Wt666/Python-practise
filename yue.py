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
# # plt.show()


# a=int(input("Enter a number:"))
# sum=0
# while a>0:
#     sum=sum+a
#     a=a-1
# print(sum)
# import numpy as np
# a=np.zeros(100)
# b=binomial=np.random.binomial(10,0.5,1000)
# print(b)
# numbers=[1,2,3,4,5324,324,324,234]
# sum=0
# for i in numbers:
#     sum=sum+i
# print(sum)

# genre=['pop','jazz','rock']
# for i in range(len(genre)): # for i in range(3): i belongs to (0-3,not include 3)
#     print('I like',genre[i])
# else:
#     print('nothing')

# a=1.3
# print(type(a))

# import Game24
# Game24.game24(2,3,4,5)



# big=max('Hello world')
# tiny=min('Hello world')
# print(tiny)
# print(big)



# print(float(99)/100)
# print(99/100)
# i=1
# print(float(i))
# print('99/100')

# sval='123'
# print(type(sval))
# print(sval+str(1))
# print(sval,1)

# x=1
# def abc():
#     print('hello world') #define a function

# abc() #use the function
# print(x)

def PLUS(a,b): # define two parameters
    c=a+b
    return c
print(PLUS(1,2))

# def greet(lang):
#     if lang == 'es':
#         print('Hola')
#     elif lang == 'fr':
#         print('Bonjour')
#     else:
#         print('Hello')
# greet('fr')
# greet('China')
# greet('es')
# def greet():
#     return 'lalala'
# print(greet())
# def greet(lang):  #lang is parameter
#     if lang == 'es':
#         return'Hola'
#     elif lang == 'fr':
#         return'Bonjour'
#     else:
#         return'Hello' # 'Hello' is result

# print(greet('japan')) #'japan' is argument




# def add(a,b):
#     c=a+b
#     return c
# print(add(2,3))
# def pay(hours,rate):
#     bill=hours*rate
#     return bill
# print(pay(45,10))
# import Pointdocstrings
# p1=Pointdocstrings.Point()
# p2=Pointdocstrings.Point()
# p1.move(2,2)
# p2.move(6,5)
# print("CALLING: P1-x, P1-y is: ", p1.x, p1.y) 
# print("CALLING: P2-x, P2-y is: ", p2.x, p2.y)
# from Pointdocstrings import Point
# p1 = Point() 
# p2 = Point()
# p1.move(2,2) 
# p2.move(6,5)
# print("CALLING: P1-x, P1-y is: ", p1.x, p1.y)
# print("CALLING: P2-x, P2-y is: ", p2.x, p2.y)
# print("CALLING: Distance from P1 to P2 is:", p1.calc_distance(p2))
fun = 6 # Global variable
# def multi():
#     fun = 6 # Local variable
#     fun = fun * 3
#     print("I am a local variable called fun inside multi = ", fun) # Print local variable
# multi()
# print("I am a global variable called fun outside multi = ", fun)
# def Greeting():
#     name = 'Mary Poppins' 
#     age = 200
#     address = 'Far Far away'
#     print(name)


# import Pointdocstrings
# p1=Pointdocstrings.Point()
import Game24
Game24.game24(4,5,6,7)



