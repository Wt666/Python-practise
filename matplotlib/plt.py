import matplotlib.pyplot as plt
x=range(-100,100)
y=[i**2 for i in x]
plt.plot(x,y,linewidth=2)
plt.title('square')
plt.savefig('result.jpg')
plt.show()