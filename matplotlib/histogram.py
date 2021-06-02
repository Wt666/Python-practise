import numpy as np
import matplotlib.pyplot as plt
# x=np.random.randn(1000)
# #plt.hist(x)
# #plt.show()
# plt.hist(x,bins=100)
# plt.show()
x1=np.random.normal(0,0.8,1000)
x2=np.random.normal(-2,1,1000)
x3=np.random.normal(3,2,1000)
kwargs=dict(bins=100,alpha=0.4)
plt.hist(x1,**kwargs)
plt.hist(x2,**kwargs)
plt.hist(x3,**kwargs)
plt.show()

