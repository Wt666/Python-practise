import pandas as pd
import numpy as np
from pandas.core.indexes import period
date=pd.date_range('20230606',periods=2)
data=pd.DataFrame(np.arange(6).reshape((2,3)),index=date,columns=list('ABC'))
print(data)