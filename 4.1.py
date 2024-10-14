import numpy as np
import matplotlib as plt

def sys(x0,v0,h,x,v):
    self_x0 = x0
    self_v0 = v0
    h = 0.1
    x0 = 0
    v0 = 0

    for i in range(0,100,1):
        x[i+1] = self_x0  + h*self_v0
        
        v[i+1] = self_v0 + h*(-0.5*self_v0 + 5)
        self_x0 = x0
        self_v0 = v0
        plt.plot(x,v,label= "eluer")
        return x , v
    print("系统位移",x);