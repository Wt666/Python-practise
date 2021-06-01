import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.histograms import _histogram_bin_edges_dispatcher
# x=[1000,1005,1010,1015,1020]
# x_labels=['1y','2y','3y','4y','5y']
# y=[1000,2000,3000,4000,5000]
# plt.bar(x,y,width=1)
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.xticks(x,x_labels) #change x to x_labels
# plt.xlabel('year')
# plt.ylabel('power')
# plt.title("wow")
# plt.show()

np.random.seed(0)
x=np.arange(5)
y=np.random.randint(-5,5,5)
print(x,y)
plt.subplot(1,2,1)
v_bar=plt.bar(x,y)
plt.axhline(0,color='blue',linewidth=2) #add the line
plt.subplot(1,2,2)
h_bar=plt.barh(x,y,color='red')
plt.axvline(0,color='red',linewidth=2)
plt.show()