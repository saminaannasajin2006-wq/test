import matplotlib.pyplot as plt
import numpy as np

x =np.array([1,2,7,20])
y =np.array([1,5,8,4])
z =np.array([2,3,7,10])

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.bar(y,x)
plt.title("bar graph")
plt.show()

a =np.array([10,50,80,40])
b =np.array([1,5,8,4])

plt.pie(a,labels=b)
plt.title("pie chart")
plt.show()

plt.scatter(a,b)
plt.title("scatter plot")
plt.show()