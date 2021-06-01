import matplotlib.pyplot as plt
import numpy as np
real_names=['千與千尋','玩具總動員4','黑衣人']
real_num1=[4444,3333,1673]
real_num2=[5453,1840,2456]
real_num3=[1223,3534,3432]
x=np.arange(len(real_names))
width=0.3
plt.bar(x,real_num1,alpha=0.5,width=0.3,label=real_names[0])
plt.bar([i+width for i in x],real_num2,alpha=0.5,width=0.3,label=real_names[1])
plt.bar([i+2*width for i in x],real_num3,alpha=0.5,width=0.3,label=real_names[2])
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
x_label=['{}th day'.format(i+1) for i in x]
plt.xticks(x,x_label)
plt.ylabel('number of tickets')
plt.legend()
plt.show()