import pandas as pd
import numpy as np
import pandas_profiling
data=pd.read_csv('/Users/wt/Documents/Python-practise/numpy and pandas/student.csv')
print(data)
pandas_profiling.ProfileReport(data)
pfr = pandas_profiling.ProfileReport(data)
pfr.to_file('reportwt.html')
print(data.describe())
#data.to_pickle('student.pickle') #output