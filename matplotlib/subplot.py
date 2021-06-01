import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(1,10,100)
plt.subplot(2,2,1)  #创建四宫格
plt.title("Sin")
plt.plot(x,np.sin(x))
plt.subplot(2,2,2)
plt.title("Tan")
plt.plot(x,np.tan(x))
plt.subplot(2,2,3)
y=[i**2 for i in x]
plt.title("square")
plt.plot(x,y)
plt.subplot(2,2,4)
plt.title("Cos")
cos_y=np.cos(x)
plt.plot(x,cos_y)
plt.show()