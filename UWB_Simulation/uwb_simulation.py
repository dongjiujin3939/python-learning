# 验证UWB测距方法
import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plot

class Uwb_Simulation:
    def __init__(self):
        # ugv质心的位置坐标
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.loaction_ugv = np.zeros((self.x0, self.y0, self.z0))
        # 小车上3个uwb节点位置坐标
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        self.location_uwb1 = np.zeros((self.x1, self.y1, self.z1))
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0
        self.loaction_uwb2 = np.zeros((self.x2, self.y2, self.z2))
        self.x3 = 0
        self.y3 = 0
        self.z3 = 0
        self.loaction_uwb3 = np.zeros((self.x3, self.y3, self.z3))
        # drone的位置坐标
        self.x_t = 0
        self.y_t = 0
        self.z_t = 0
        self.location_drone = np.zeros((self.x_t, self.y_t, self.z_t))
        # drone 到三个uwb节点的距离
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
    
    def Fomulation_Solve(self, a1, b1, c1, a2, b2, c2):
        denominator = a1*b2 -a2*b1
        if denominator == 0:
            return "no only solution"
        x = (c1*b1 - c2*b1)/denominator
        y = (a1*c2 - a2*c1)/denominator
        return x,y


    def Distance_Measured(self):
        # ugv 质心
        self.x0 = 0.2
        self.y0 = 0
        self.z0 = 0.1
        self.location_ugv = np.array([self.x0, self.y0, self.z0])
        # 三个uwb锚点的位置坐标
        self.x1 = 0
        self.y1 = 0.2
        self.z1 = 0.1
        self.location_uwb1 = np.array([self.x1, self.y1, self.z1])
        self.x2 = 0
        self.y2 = -0.2
        self.z2 = 0.1
        self.loaction_uwb2 = np.array([self.x2, self.y2, self.z2])
        self.x3 = 0.4
        self.y3 = -0.2
        self.z3 = 0.1
        self.location_uwb3 = np.array([self.x3, self.y3, self.z3])
        # ugv 地系坐标
        self.x_t = 5
        self.y_t = 5
        self.z_t = 5.1
        # 计算uav到各个锚点的距离
        self.d1 = math.sqrt((self.x_t - self.x1)**2 + (self.y_t - self.y1)**2 + (self.z_t -self.z1)**2)
        self.d2 = math.sqrt((self.x_t - self.x2)**2 + (self.y_t - self.y2)**2 + (self.z_t -self.z2)**2)
        self.d3 = math.sqrt((self.x_t - self.x3)**2 + (self.y_t - self.y3)**2 + (self.z_t -self.z3)**2)
        print(self.d1, self.d2, self.d3)
        #分别以三个锚点的坐标为圆心，到uav的距离为半径得到三个球并求交点获得uav计算出来的坐标
        self.x_c, self.y_c = self.Fomulation_Solve(2*(self.x2 - self.x1), 2*(self.y2-self.y1), self.d1**2 - self.d2**2 +(self.x2 - self.x1)**2 + (self.y2 - self.y1)**2, 2*(self.x3 - self.x1), 2*(self.y3 - self.y1), self.d1**2 - self.d3**2 + (self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)
        self.z_c = math.sqrt(self.d1**2 - (self.x_c - self.x1)**2 - (self.y_c - self.y1)**2) + self.z1
        print(self.x_c, self.y_c, self.z_c)

if __name__ == "__main__":
    uwb = Uwb_Simulation()
    uwb.Distance_Measured()


