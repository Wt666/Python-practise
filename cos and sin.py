import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
sin_y=np.sin(x)
plt.plot(x,sin_y)
cos_y=np.cos(x)
plt.plot(x,cos_y)
plt.show()