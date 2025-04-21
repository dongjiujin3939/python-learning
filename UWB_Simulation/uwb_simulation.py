# 验证UWB测距方法
import math
import numpy as np
import matplotlib.pyplot as plt
from LM import LM3DPositioning

class Uwb_Simulation:
    def __init__(self):
        # ugv质心的位置坐标
        self.x0 = 0.2
        self.y0 = 0
        self.z0 = 0.1
        self.location_ugv = np.array([self.x0, self.y0, self.z0])
        # 小车上3个uwb节点位置坐标
        self.x1 = 0
        self.y1 = 0.2
        self.z1 = 0.1
        self.location_uwb1 = np.array([self.x1, self.y1, self.z1])
        self.x2 = 0
        self.y2 = -0.2
        self.z2 = 0.1
        self.location_uwb2 = np.array([self.x2, self.y2, self.z2])
        self.x3 = 0.4
        self.y3 = -0.2
        self.z3 = 0.1
        self.location_uwb3 = np.array([self.x3, self.y3, self.z3])
        # drone的位置坐标
        self.x_t = 0
        self.y_t = 0
        self.z_t = 0
        self.location_drone = np.array([self.x_t, self.y_t, self.z_t])
        # drone 到三个uwb节点的距离
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        #记录数据
        self.time_step = []
        self.true_position = []
        self.caculated_position = []

    # 解析解解法
    # def Fomulation_Solve(self, a1, b1, c1, a2, b2, c2):
    #     denominator = a1*b2 -a2*b1
    #     if denominator == 0:
    #         return "no only solution"
    #     x = (c1*b2 - c2*b1)/denominator
    #     y = (a1*c2 - a2*c1)/denominator
    #     return x,y


    def Distance_Measured(self, t):
        # uav 地系坐标
        self.x_t = 5 + 0.1 * t
        self.y_t = 5 + 0.2 * t
        self.z_t = 5.1 + 0.05 * t
        # 计算uav到各个锚点的距离
        self.d1 = math.sqrt((self.x_t - self.x1)**2 + (self.y_t - self.y1)**2 + (self.z_t -self.z1)**2)
        self.d2 = math.sqrt((self.x_t - self.x2)**2 + (self.y_t - self.y2)**2 + (self.z_t -self.z2)**2)
        self.d3 = math.sqrt((self.x_t - self.x3)**2 + (self.y_t - self.y3)**2 + (self.z_t -self.z3)**2)
        #分别以三个锚点的坐标为圆心，到uav的距离为半径得到三个球并求交点获得uav计算出来的坐标
        # print(self.d1, self.d2, self.d3)
        # self.x_c, self.y_c = self.Fomulation_Solve(2*(self.x2 - self.x1), 2*(self.y2-self.y1), self.d1**2 - self.d2**2 +(self.x2 - self.x1)**2 + (self.y2 - self.y1)**2, 2*(self.x3 - self.x1), 2*(self.y3 - self.y1), self.d1**2 - self.d3**2 + (self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)
        # self.z_c = math.sqrt(self.d1**2 - (self.x_c - self.x1)**2 - (self.y_c - self.y1)**2) + self.z1
        anchors = [
            self.location_uwb1,
            self.location_uwb2,
            self.location_uwb3
        ]

        true_pos = [self.x_t, self.y_t, self.z_t]
        distances = [self.d1, self.d2, self.d3]
        lm = LM3DPositioning(anchors, true_pos)
        initial_guess = [0.0, 0.0, 1.0]
        estimated = lm.levenberg_marquardt(distances, initial_guess, verbose = True)
        print("Estimated Position:", estimated)
        if t == 99:
            lm.visualize_3d(estimated)

        self.time_step.append(t)
        self.true_position.append((self.x_t, self.y_t, self.z_t))
        self.caculated_position.append(tuple(estimated))

    def plot_results(self):
        true_position = np.array(self.true_position)
        caculated_position = np.array(self.caculated_position)
        
        fig, axes = plt.subplots(3, 1, figsize = (10, 8))
        labels = ['X Position', 'Y Position', 'Z Position']
        for i in range(3):
            axes[i].plot(self.time_step, true_position[:,i], label = 'True Postion', linestyle = '-',)
            axes[i].plot(self.time_step, caculated_position[:,i], label = 'Caculated Position', linestyle = '--')
            axes[i].set_ylabel(labels[i])
            axes[i].legend()
            axes[i].grid()
        
        axes[2].set_xlabel('time step')
        plt.suptitle('True and Estimated UAV position')
        plt.show()

if __name__ == "__main__":
    uwb = Uwb_Simulation()
    for t in range(0,100):
        uwb.Distance_Measured(t)
    uwb.plot_results()


