import numpy as np
import matplotlib.pyplot as plt

def euler_method(f,x0,y0,h,n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = x0
    y[0] = y0
    
    for i in range(n):
        y[i+1] = y[i] + h * f(x[i],y[i])
        x[i+1] = x[i] + h
    return x , y
def f(x,y):
    return x + y # 定义微分方程

x0 = 0
y0 = 1
h = 0.1
n = 50

x, y = euler_method(f,x0,y0,h,n)

plt.plot(x,y,label = 'Numerical solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()