import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.nanfunctions import _nanvar_dispatcher
import pandas as pd
import pandas_datareader
import datetime as dt
import pandas_datareader.data as web
start=dt.datetime(2011,6,21)
end=dt.datetime(2021,6,21)
nvda=web.DataReader('NVDA','yahoo',start,end)
# print(nvda.head(10))
msft=web.DataReader('MSFT','yahoo',start,end)
tesla=web.DataReader('TSLA','yahoo',start,end)
# nvda['Open'].plot(label = 'NVDA',figsize=(16,8),title='Open Price')
# plt.show()
nvda['Open'].plot(label = 'NVDA',figsize=(16,8),title='Open Price')
msft['Open'].plot(label = 'MSFT',figsize=(16,8))
tesla['Open'].plot(label = 'TSLA',figsize=(16,8),color='r',linewidth=5.0,linestyle='--')
plt.legend(loc='best') # set category
plt.show() #show the pic