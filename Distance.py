
import numpy as np
import math
p1=np.array([3,4])
p2=np.array([4,3])
p3=p2-p1
p4=math.hypot(p3[0],p3[1])
print(p4)
