# %matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [10,8]  # Set default figure size
import requests
s1=pd.Series(np.random.randn(100),name='abc')
print(s1.describe())
# s1.index=['a','b','c','d']
# print('a' in s1)
df=pd.read_csv('/Users/wt/Desktop/test_pwt.csv')
print(type(df))
print(df[2:4])
print(df.iloc[2:5,0:4])
print(df.loc[df.index[2:5],['country','tcgdp']])
df2=df[['country','POP','tcgdp']]
df2=df2.set_index('country')
df2.columns=['Population','Total GDP']
df2['Population']=df2['Population']*1e3
df2['Per Capita GDP']=df2['Total GDP']*1e6/df2['Population']
df2=df2.sort_values(by='Per Capita GDP',ascending=False)
print(df2)
ax=df2['Per Capita GDP'].plot(kind='bar')
ax.set_xlabel('Country',fontsize=12)
ax.set_ylabel('Per Capita GDP',fontsize=12)
plt.show()


r = requests.get('http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv')
print(r)
url = 'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
source = requests.get(url).content.decode().split("\n")
print(source[0])
print(source[1])
# data=pd.read_csv(url,index_col=0,parse_dates=True)
# print(type(data))
# print(data.head())
