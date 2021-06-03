from numpy.core.defchararray import index
from numpy.core.numeric import outer
import pandas as pd
import numpy as np
#concatenating
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
df4=pd.DataFrame(np.ones((3,4))*3,columns=['b','c','d','e'])
print(df1,df2,df3)
res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res)

#join,["'inner",'outer']
print(df1)
print(df4)
resl=pd.concat([df1,df4],join='inner',ignore_index=True)
print(resl)
# res1=pd.concat([df1,df4],axis=1,join_axes=[df1.index])
# print(res1)
res1=df1.append([df2,df3],ignore_index=True)
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(res1)
print(s1)
res2=df1.append(s1,ignore_index=True)
print(res2)