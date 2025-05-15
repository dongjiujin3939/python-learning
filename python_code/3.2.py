import numpy as np  # 用np调用numpy库中的函数

def sys(f,t,miu,u): # 定义一个新的函数sys
    x,v = f # 定义x,v为因变量为f的微分方程
    dydt =  [v,-miu*v+u] # 微分方程表达式右边等式部分
    return dydt # sys 返回该微分方程组的值

miu = -0.5
u = 5.0
f0 = [0.0,0.0]
t = np.linspace(0,1,101) # 数值解的范围1为间隔0到101

from scipy.integrate import odeint # 调用odeint函数

sol = odeint(sys,f0,t,args=(miu,u)) # 解微分方程组的值
print("该系统的数值解为",sol)

import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='x(t)')
plt.plot(t, sol[:, 1], 'g', label='v(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
