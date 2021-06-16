import pandas as pd
import numpy as np
import pandas_profiling
df=pd.read_csv('/Users/wt/Documents/Python-practise/numpy and pandas/property-data.csv')
x = df["ST_NUM"].mean()

df["ST_NUM"].fillna(x, inplace = True)

print(df.to_string())


data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df1 = pd.DataFrame(data, index = ["day1", "day2", "day3"])

df1['Date'] = pd.to_datetime(df1['Date'])

print(df1.to_string())

person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}

df3 = pd.DataFrame(person)

df3.loc[2, 'age'] = 30 # 修改数据

print(df3.to_string())

person1 = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]    
}

df2 = pd.DataFrame(person1)

for x in df2.index:
  if df2.loc[x, "age"] > 120:
    df2.loc[x, "age"] = 120

print(df2.to_string())