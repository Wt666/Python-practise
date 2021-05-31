#print("I'm\" apple")
#print("apple"+"4")
#print("1.2+2")
#print(int("1")+2)
#print(float("1.2")+3)
#print(2**3)
#print(8%5)
#print(8//5)
#wangtong=1*2
#aw=wangtong/2
#print(wangtong,aw)
#condition=1
#while condition<10:
#    print(condition)
#    condition=condition+1
#while false:
#    print("I'm puxinnan")
import numpy as np
import random
example_list=[1,2,3,4,5,6,7,12,543,876,12,3,2,5]
#for i in example_list:
#   print(i)
 #   print('inner of for')
#print("outer of fot")
a=random.randint(1,50)
b=25
if a<b:
    for i in example_list:
        if a < i:
            print(i)
        else:
            print("A="+str(a))
elif a==b:
    print("EQUAL")
else:
    print("B="+b)


