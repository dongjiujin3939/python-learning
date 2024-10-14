import numpy as np
import matplotlib.pyplot as plt

def euler_method_second_order(f,g,x0,y0,z0,h,n):
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    z = np.zeros(n+1)

    x[0] = x0
    y[0] = y0
    z[0] = z0

    for i in range(n):
        y[i+1] = y[i] + h * f(x[i],y[i],z[i])
        z[i+1] = z[i] + h * g(x[i],y[i],z[i])
        x[i+1] = x[i] + h
    return x,y

def f(x,y,z):
    return z
def g(x,y,z):
    return -y

x0 = 0
y0 = 1
z0 = 0
h = 0.1
n = 100

x,y = euler_method_second_order(f,g,x0,y0,z0,h,n)

plt.plot(x,y,label = '二阶微分方程数值解')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()