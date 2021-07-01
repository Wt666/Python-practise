import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader
import datetime as dt
import pandas_datareader.data as web
from pandas.plotting import scatter_matrix
start=dt.datetime(2011,6,21)
end=dt.datetime(2021,6,21)
nvda=web.DataReader('NVDA','yahoo',start,end)
print(nvda.tail(10))
msft=web.DataReader('MSFT','yahoo',start,end) #6060.hk
tesla=web.DataReader('TSLA','yahoo',start,end)
print(msft.head(10))
nvda['Open'].plot(label='NVDA',figsize=(16,8),title='Open price',color='r')
msft['Open'].plot(label='MSFT')
plt.legend()
tech_comp=pd.concat([nvda['Close'],msft['Close'],tesla['Close']],axis=1)
tech_comp.columns=['NVDA Close','MSFT Close','Teslaa Close']
scatter_matrix(tech_comp,figsize=(10,10),alpha=0.2,hist_kwds={'bins':50})
plt.show()
