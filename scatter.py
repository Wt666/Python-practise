import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size
# x=np.linspace(0,10,100)
# sin_y=np.sin(x)
# plt.plot(x,sin_y,'o') same as next line
# plt.scatter(x,sin_y,linewidths=1,)
# plt.show()

np.random.seed(0)
a=np.random.rand(100)
b=np.random.rand(100)
#size=np.random.rand(10)*1000
size=np.random.rand(100)*1000
color=np.random.rand(100)
#print(x)
plt.scatter(a,b,s=size,c=color,alpha=0.7)
plt.show()
