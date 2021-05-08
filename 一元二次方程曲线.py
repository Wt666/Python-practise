import matplotlib.pyplot as plt
import numpy as np
x=range(-100,100)
y=[i**2 for i in x]

plt.xlabel("X")
plt.ylabel("Y")
plt.rcParams['font.sans-serif']=['SimHei'] # set Chinese to show
plt.rcParams['axes.unicode_minus']=False
plt.title('一元二次方程')
plt.plot(x,y,linewidth=33)
plt.plot(x,y)
plt.show()

