from numpy.core.defchararray import array
import pandas as pd
import numpy as np
dates=pd.date_range('20210603',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2]=1111
df.loc['20210604','B']=222222
#df.A[df.A>4]=0 #similar like SQL
df.B[df.A>4]=0
df['F']=np.nan
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20210603',periods=6))
print(df)