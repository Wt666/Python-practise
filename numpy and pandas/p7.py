import pandas as pd
import numpy as np
#merging two df by key/keys.(may be used in databse)
#simple example
left = pd.DataFrame({'key':['K0','K1','K2','K3'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
print(left)
print(right)
res=pd.merge(left,right,on='key')
print(res)
#consider two keys
left1 = pd.DataFrame({'key1':['K0','K0','K1','K2'],'key2':['K0','K1','K0','K1'],'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3']})
right1 = pd.DataFrame({'key1':['K0','K1','K1','K2'],'key2':['K0','K0','K0','K0'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']})
print(left1)
print(right1)
#how=['left,right,outer,inner']
res1=pd.merge(left1,right1,on=['key1','key2'],how='outer',indicator='indicator_column')
print(res1)

left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                                  'B': ['B0', 'B1', 'B2']},
                                  index=['K0', 'K1', 'K2'])
right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                                     'D': ['D0', 'D2', 'D3']},
                                      index=['K0', 'K2', 'K3'])
print(left2)
print(right2)
# left_index and right_index
res2 = pd.merge(left2, right2, left_index=True, right_index=True, how='outer')
res4 = pd.merge(left2, right2, left_index=True, right_index=True, how='inner')
print('res2=',res2)
print('res4=',res4)

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res3 = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
res5 = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='outer')
print(res3)
print(res5)