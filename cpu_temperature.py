
import numpy as np 
import matplotlib.pyplot as plt
import random

ls = list()
for i in range(1000):
    rn = random.randint(1, 10)
    fun = (i**2//rn)*2*np.pi
    ls.append(fun)
plt.plot(ls)
plt.show()