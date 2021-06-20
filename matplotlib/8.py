import matplotlib.pyplot as plt
import numpy as np
X=np.arange(12)
Y1=(1-X/float(12))*np.random.uniform(0.5,1.0,12)
Y2=(1-X/float(12))*np.random.uniform(0.5,1.0,12)
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
for x,y in zip(X,Y1):
    #ha:horizontal alignment
    plt.text(x+0.04,y+0.05,'%.2f'%y,ha='center',va='bottom')
for x,y in zip(X,Y2):
    #ha:horizontal alignment
    plt.text(x+0.04,-y-0.05,'-%.2f'%y,ha='center',va='top')
plt.show()


