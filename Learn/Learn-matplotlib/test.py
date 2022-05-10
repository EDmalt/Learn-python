# By hefei
# @File : test.py
import numpy as np
import matplotlib.pyplot as plt
a=np.array([[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]])
plt.plot(a[0],a[1],color="green",linewidth=10,linestyle=":",marker="s")
plt.xlabel("test-x",fontsize=20,color="blue")
plt.ylabel("test-y",fontsize=20,color="red")
plt.show()
