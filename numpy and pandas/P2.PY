from numpy.core.defchararray import array
import pandas as pd
import numpy as np
dates=pd.date_range('20210603',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
print(df['A'],df.A)
print(df[0:3],df['20210602':'20210603'])
#select by label: loc
print(df.loc['20210604'])
print(df.loc['20210604',['A','B']])
#select by position: iloc
print(df.iloc[3:5,1:3])
print(df.iloc[[1,3,5],1:3])
#mixed selection: ix
#print(df.ix[:3,['A','C']])

#Boolean indexing
print(df[df.A>8])