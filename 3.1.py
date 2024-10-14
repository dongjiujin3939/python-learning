import numpy as np  # 使用np调用numoy库中的函数 as的作用就相当于一个赋值操作，np就作为numpy的对象


def pend(y, t, b, c): # 创建一个新的 pend 函数包括4个参数 y,t,b,c
    theta, omega = y # 将theta,omega 定义为因变量y的微分方程组
    dydt = [omega, -b*omega - c*np.sin(theta)] # 微分方程组的表达式 每个向量是方程的右半部分
    return dydt # 语句最终返回微分方程组dydt的值

b = 0.25
c = 5.0 # 定义 b,c的值
y0 = [np.pi - 0.1, 0.0] # 赋予微分方程初值 pi - 0.1，0.0分别为两个微分方程0时刻的初值
t = np.linspace(0, 10, 101) # 规定数值解的范围
from scipy.integrate import odeint # 引入scipy.integrate 中的odeint 函数
sol = odeint(pend, y0, t, args=(b, c)) # 使用odeint函数解微分方程 args=(b, c)表示将b,c的值传递到pend这个函数中
print("该微分方程的解为",sol)

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show() # 绘图