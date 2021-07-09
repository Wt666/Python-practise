# # %matplotlib inline
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# plt.rcParams["figure.figsize"] = [10,8]  # Set default figure size
# import requests
# # s1=pd.Series(np.random.randn(100),name='abc')
# # print(s1.describe())
# # # s1.index=['a','b','c','d']
# # # print('a' in s1)
# # df=pd.read_csv('/Users/wt/Desktop/test_pwt.csv')
# # print(type(df))
# # print(df[2:4])
# # print(df.iloc[2:5,0:4])
# # print(df.loc[df.index[2:5],['country','tcgdp']])
# # df2=df[['country','POP','tcgdp']]
# # df2=df2.set_index('country')
# # df2.columns=['Population','Total GDP']
# # df2['Population']=df2['Population']*1e3
# # df2['Per Capita GDP']=df2['Total GDP']*1e6/df2['Population']
# # df2=df2.sort_values(by='Per Capita GDP',ascending=False)
# # print(df2)
# # ax=df2['Per Capita GDP'].plot(kind='bar')
# # ax.set_xlabel('Country',fontsize=12)
# # ax.set_ylabel('Per Capita GDP',fontsize=12)
# # plt.show()


# # r = requests.get('http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv')
# # print(r)
# # url = 'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
# # source = requests.get(url).content.decode().split("\n")
# # print(source[0])
# # print(source[1])
# # data=pd.read_csv(url,index_col=0,parse_dates=True)
# # print(type(data))
# # print(data.head()) #cuz the network, it doesn't work.
# s1=pd.Series(np.random.randn(1000))
# s2=pd.Series(np.random.randn(1000))
# print(s1.cov(s2))
# x=np.linspace(0,10,1000)
# y=np.power(x,2)
# y1=np.power(x,3)
# plt.xlim(1,5)
# plt.ylim(0,30)
# plt.plot(x,y,'b-',label='2')
# plt.plot(x,y1,'--',label='3',color='r')
# plt.tight_layout()
# plt.legend()
# plt.show()
# def printMove(fr, to):
#     print( 'move from ' + str(fr) + ' to ' + str(to))

# def Towers(n, fr, to, spare):
#     if n == 1:
#         printMove(fr, to)
#     else:
#             Towers(n - 1, fr, spare, to)
#             Towers(1, fr, to, spare)
#             Towers(n - 1, spare, to, fr)
# array=[1,2,5,3,6,8,4]
# for i in range(len(array)-1,0,-1):
#     print('i:',i)
#     for j in range(0,i):
#         print('j:',j)
#         if array[j]>array[j+1]:
#             array[i],array[j+1]=array[j+1],array[j]
# print(array)
# try:
#     a=int(input())
#     b=int(input())
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print('ZDE Wrong')
# except ValueError:
#     print('unsupported operation')
# from os import close


# try:
#     fh=open('testfile','r')
#     fh.read()
# except IOError:
#     print('no')
# else:
#     print('yes')
# fh.close()

# try:
#     print('try block')
#     a=int(input())
#     b=int(input())
#     c=a/b
# except ZeroDivisionError:
#     print('ZDE IS Wrong')
# except ValueError:
#     print('unsupported operation')
# else:
#     print('else block')
#     print('Division=',c)
# finally:
#     print('finally block')
#     a=0
#     b=0
# print('out of try, except, else and finally block')

# def geek_message():
#     try:
#         geek='GeeksForGeeks'
#         return geeksforgeeks  #the correct code: return geek
#     except NameError:
#         return ("NameError occured, some variable is not defined")
# print(geek_message())

# try:
#     x=int(input('enter a number up to 100:'))
#     if x>100:
#         raise ValueError
# except ValueError:
#     print(x, 'is outof allowed range')
# else:
#     print(x, 'is within the range')
# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError as e: # e is the storage of error value
#         print('The argument does not contain numbers\n',e)
#     finally:
#         print('it is done')
# print(temp_convert(5.6))

def printMove(fr, to):
    print('move from '+str(fr)+' to '+str(to))
def Towers(n,fr,spare,to):
    count=0
    if n==1:
        printMove(fr,to)
        return 1
    else:
        count +=Towers(n-1,fr,spare,to) #let n-1 disk move to b
        count +=Towers(1,fr,to,spare) # let n disk from a move to c
        count +=Towers(n-1,spare,to,fr) #let n-1 for b move to c
        return count
print(Towers(3,'A','B','C'))

def Move_Towers(n,a,b,c):
    count=0
    if n==1:
        print('move from '+a+' to '+c)
        return 1
    else:
        count +=Move_Towers(n-1,a,c,b)
        count +=Move_Towers(1,a,b,c)
        count +=Move_Towers(n-1,b,c,a)
        return count
print(Move_Towers(3,'a','b','c'))