import numpy as np
import matplotlib.pyplot as plt


if __name__=='__main__' :
  x = np.array([1,2,3,4,5])
  y = np.array([6,7,1,2,3])
  plt.scatter(x=x, y=y)
  plt.show()