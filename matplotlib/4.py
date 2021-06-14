import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],[r'$Really\ bad$',r'$bad\ \alpha$',r'$Normal$',r'$good$',r'$very\ good$'])
line1,=plt.plot(x,y2,label='up')
line2,=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
plt.legend(handles=[line1,line2,],labels=['aaa','bbb'], loc='best')
plt.show()
