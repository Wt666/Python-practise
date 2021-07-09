# from itertools import permutations
# a=permutations([1,2,3,4])
# for i in list(a):
#     print(*i,sep='')

# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and b!=c and c!=a:
#                 print(a,b,c,sep='')
'''
顺序输出
'''
# from typing import Sequence
# import numpy as np
# a=int(input("First input"))
# b=int(input("Second input"))
# c=int(input("Third input"))
# list=[a,b,c]
# print(*np.sort(list),sep=',')

# len = []
# k = int(input("请输入比较的数字数目："))
# for i in range(k):
#     k = int(input("请逐个输入比较的数字："))
#     len.append(k)
# len.sort()
# print("比较后从小到大排序为："+str(len))

# '''
# 输入某年某月某日，判断这一天是这一年的第几天？
# '''
# year = int(input("请输入年份："))
# month = int(input("请输入月份："))
# day =  int(input("请输入某一个月份的天数："))
# #将月份逐渐相加添加到列表中
# months = [0,31,59,90,120,151,181,212,243,273,304,334]
# if 0 < month <= 12:
#     sum = months[month-1]
# else:
#     print("超出了年份的范围，年月份是你家定的啊!")
# sum += day
# if ((year % 400 == 0) or (year %4 == 0) and (year % 100 != 0)):
#     if(month > 2):
#         sum += 1
# print('这一天是这一年的%d日'%sum)

# import numpy as np
# A = np.arange(12).reshape(4,3)
# print(A)
# for a in A:
#     a = a + 1
#     print(a)

# B = np.arange(12).reshape(4,3)
# for b in B:
#     b += 1
#     print(b)

# n=int(input("input the exact number of Fibonacci sequence"))
# def find(n):
#     if n==2 or n==3:
#         return 1
#     elif n==1:
#         return 0
#     else:
#         return find(n-1)+find(n-2)
# print(find(n))
# class Caculator:
#     name='gg'
#     price=19

#     def add(self,x,y):
#         print(self.name)
#         print(x+y)
# cal=Caculator()
# print(cal.name)
# cal.add(10,11)
# dict1={'Name':'WT','Gender':'MALE'}
# dict1.update({'HOME':'KF'})
# print(dict1)

# dict1={'Name':'WT','Gender':'MALE'}
# dict2={'HOME':'KF'}
# dict1.update(dict2)
# print(dict1)
# print(dict1.keys())

# num=int(input('enter a number:')) #initialize a number
# sum=0
# while (num>0):
#     sum += num
#     num=num-1
# print(sum)

# 题目5：将一个列表的数据复制到另一个列表中。
list1=[1,2,3,4,5]
list2=list1.copy()
print(list2)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
cla = [1,2,3,4,5,6,7,8,9]
alc = []
i = 0
while (len(alc) < len(cla)):
    alc.append(cla[i])
    i = i + 1
print(alc)

a = [1, 2, 3]
b = a[:]
print(b)

# -*- coding: UTF-8 -*-
#将列表复制到另一个列表里
a = [1,2,3,4,5,6,7,8,9]
b = a*1
print(b)

# 题目6：输出 9*9 乘法口诀表。 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('\'i\'*\'j\''+str(i*j))
#     print()
#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d" % (i,j,i*j),end = " ")
    print() 

# 题目7：暂停一秒输出。 程序分析：使用 time 模块的 sleep() 函数。 
# from time import sleep
# a=[1,2,3,4]
# for i in a:
#     print(i)
#     sleep(2) #set output interval 

# 题目8：暂停一秒输出，并格式化当前时间。
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import time
 
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
 
# # 暂停一秒
# # time.sleep(1)
 
# # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
 #!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
while True: 
    # 暂停一秒
    time.sleep(1)
 
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
