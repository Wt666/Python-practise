import matplotlib.pyplot as plt
import numpy as np
from numpy.core.function_base import linspace
x=np.linspace(0,10,100)
plt.plot(x,x+0,'pg')
plt.plot(x,x+2,'-.b')
plt.show()