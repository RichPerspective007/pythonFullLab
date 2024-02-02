import matplotlib.pyplot as plt
import numpy as np

o_n = np.array([i for i in range(250)])
o_n2 = np.array([i**2 for i in range(50)])

plt.plot(o_n,label='O(n)', color='springgreen')
plt.plot(o_n2,label='O(n^2)', color='red')

plt.title("O(n) vs O(n^2)")
plt.xlabel('Input Size')
plt.ylabel('Steps')

plt.xticks(np.arange(0,250,5))
plt.yticks(np.arange(0,2500,100))
plt.legend()
plt.show()