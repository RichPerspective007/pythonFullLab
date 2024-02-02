import matplotlib.pyplot as plt
import numpy as np
from random import *

#creating an array of x-coordinates
x_points = np.array([randint(0,100) for i in range(30)])

#creating an array of y-coordinates
y_points = np.array([randint(0,100) for i in range(30)])

#creating the plot
plt.scatter(x_points,y_points,color='b')
plt.plot(x_points,y_points,'o',color='r')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()