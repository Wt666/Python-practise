from numpy.core.defchararray import array
import pandas as pd
import numpy as np
dates=pd.date_range('20210603',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan

print(df.dropna(axis=0,how='any')) #how={'any','all'} axis=0 means row
print(df.dropna(axis=1,how='any'))
print(df.fillna(value=99999))
print(df.isnull())
print(np.any(df.isnull())==True)
