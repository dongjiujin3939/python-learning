import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos,tan


class DroneControlSim:
    def __init__(self): # 定义初始化函数
        self.sim_time = 10
        self.sim_step = 0.002
        self.drone_states = np.zeros((int(self.sim_time/self.sim_step), 12)) # np.zeros()函数创建指定形状的数组
        self.time= np.zeros((int(self.sim_time/self.sim_step),)) # 一维数组
        self.rate_cmd = np.zeros((int(self.sim_time/self.sim_step), 3))  # 角速率
        self.attitude_cmd = np.zeros((int(self.sim_time/self.sim_step), 3)) # 姿态角
        self.velocity_cmd = np.zeros((int(self.sim_time/self.sim_step), 3)) # 速度
        self.position_cmd = np.zeros((int(self.sim_time/self.sim_step), 3)) # 位置
        self.pointer = 0 # 指针

        self.I_xx = 2.32e-3
        self.I_yy = 2.32e-3
        self.I_zz = 4.00e-3
        self.m = 0.5
        self.g = 9.8
        self.I = np.array([[self.I_xx, .0,.0],[.0,self.I_yy,.0],[.0,.0,self.I_zz]]) #np.array函数 创建数组


    def run(self): # 方法
        for self.pointer in range(self.drone_states.shape[0]-1): # 循环除最后一个状态的所有状态
            self.time[self.pointer] = self.pointer * self.sim_step # 存储当前时间
            # print(self.pointer)
            thrust_cmd = 0.0 # 初始化升力
            M = np.zeros((3,)) # 三轴力矩

            if self.pointer == 0:
                self.drone_states[self.pointer,:] = 0
            else:
                self.drone_states[self.pointer+1,:] = self.drone_states[self.pointer,:] + self.sim_step * drone_states

            attitude_cmd = [1,1,1]
            self.attitude_cmd[self.pointer,[0,1,2]] = attitude_cmd
            rate_cmd = self.attitude_controller(attitude_cmd)
            Mq = self.rate_controller(rate_cmd)
            drone_states = self.drone_dynamics(self.thrust_cmd,Mq)
            # print(self.drone_states)


        

        self.time[-1] = self.sim_time # 将仿真时间赋给数组最后一个元素，该数组最后一位反映整个仿真时间
        
        
        

    def drone_dynamics(self,T,M):
        # Input:
        # T: float Thrust
        # M: np.array (3,)  Moments in three axes
        # Output: np.array (12,) the derivative (dx) of the drone 
        
        x = self.drone_states[self.pointer,0]
        y = self.drone_states[self.pointer,1]
        z = self.drone_states[self.pointer,2]
        vx = self.drone_states[self.pointer,3]
        vy = self.drone_states[self.pointer,4]
        vz = self.drone_states[self.pointer,5]
        phi = self.drone_states[self.pointer,6]
        theta = self.drone_states[self.pointer,7]
        psi = self.drone_states[self.pointer,8]
        p = self.drone_states[self.pointer,9]
        q = self.drone_states[self.pointer,10]
        r = self.drone_states[self.pointer,11] # 12个状态量

        R_d_angle = np.array([[1,tan(theta)*sin(phi),tan(theta)*cos(phi)],\
                             [0,cos(phi),-sin(phi)],\
                             [0,sin(phi)/cos(theta),cos(phi)/cos(theta)]]) # 姿态角变化率和角速率之间的关系矩阵


        R_E_B = np.array([[cos(theta)*cos(psi),cos(theta)*sin(psi),-sin(theta)],\
                          [sin(phi)*sin(theta)*cos(psi)-cos(phi)*sin(psi),sin(phi)*sin(theta)*sin(psi)+cos(phi)*cos(psi),sin(phi)*cos(theta)],\
                          [cos(phi)*sin(theta)*cos(psi)+sin(phi)*sin(psi),cos(phi)*sin(theta)*sin(psi)-sin(phi)*cos(psi),cos(phi)*cos(theta)]]) # 机体系到地系的旋转矩阵

        d_position = np.array([vx,vy,vz]) 
        d_velocity = np.array([.0,.0,self.g]) + R_E_B.transpose()@np.array([.0,.0,T])/self.m 
        d_angle = R_d_angle@np.array([p,q,r])
        d_q = np.linalg.inv(self.I)@(M-np.cross(np.array([p,q,r]),self.I@np.array([p,q,r]))) # @表示矩阵乘法
        # print(q)
        dx = np.concatenate((d_position,d_velocity,d_angle,d_q)) # np.concatenate函数连接多个数组
        return dx 


    def rate_controller(self,cmd):
        # Input: cmd np.array (3,) rate commands
        # Output: M np.array (3,) moments
        
        error = 0
        kp = 0.024
        error = cmd - self.drone_states[self.pointer,[9,10,11]]
        output_p = kp * error
        
        self.thrust_cmd= -9.8
        # print(M)
        return output_p


    def attitude_controller(self,cmd):
        # Input: cmd np.array (3,) attitude commands
        # Output: M np.array (3,) rate commands

        # roll & pitch
        kp = 1.0
        error = 0.0
        error = cmd[0] - self.drone_states[self.pointer,6]
        roll_output = kp * error
        error = cmd[1] - self.drone_states[self.pointer,7]
        pitch_output = kp * error
        # yaw
        kp_y = 5.0
        error= cmd[2] - self.drone_states[self.pointer,8]
        yaw_output = kp_y * error
        output = [roll_output,pitch_output,yaw_output]
        self.rate_cmd[self.pointer,[0,1,2]] = output
        return output


    def velocity_controller(self,cmd):
        # Input: cmd np.array (3,) velocity commands
        # Output: M np.array (2,) phi and theta commands and thrust cmd
        pass




    def position_controller(self,cmd):
        # Input: cmd np.array (3,) position commands
        # Output: M np.array (3,) velocity commands
        pass


    def plot_states(self):
        fig1, ax1 = plt.subplots(4,3) # 4x3的子图
        self.position_cmd[-1] = self.position_cmd[-2] # 将倒数第二个位置的值赋给末尾
        ax1[0,0].plot(self.time,self.drone_states[:,0],label='real')
        ax1[0,0].plot(self.time,self.position_cmd[:,0],label='cmd')
        ax1[0,0].set_ylabel('x[m]')
        ax1[0,1].plot(self.time,self.drone_states[:,1])
        ax1[0,1].plot(self.time,self.position_cmd[:,1])
        ax1[0,1].set_ylabel('y[m]')
        ax1[0,2].plot(self.time,self.drone_states[:,2])
        ax1[0,2].plot(self.time,self.position_cmd[:,2])
        ax1[0,2].set_ylabel('z[m]')
        ax1[0,0].legend() # 第一行的三个图分别表示x,y,z三个方向上的位置目标指令和实际位置的曲线图

        self.velocity_cmd[-1] = self.velocity_cmd[-2]
        ax1[1,0].plot(self.time,self.drone_states[:,3])
        ax1[1,0].plot(self.time,self.velocity_cmd[:,0])
        ax1[1,0].set_ylabel('vx[m/s]')
        ax1[1,1].plot(self.time,self.drone_states[:,4])
        ax1[1,1].plot(self.time,self.velocity_cmd[:,1])
        ax1[1,1].set_ylabel('vy[m/s]')
        ax1[1,2].plot(self.time,self.drone_states[:,5])
        ax1[1,2].plot(self.time,self.velocity_cmd[:,2])
        ax1[1,2].set_ylabel('vz[m/s]') # 三个方向上的速度

        self.attitude_cmd[-1] = self.attitude_cmd[-2]
        ax1[2,0].plot(self.time,self.drone_states[:,6])
        ax1[2,0].plot(self.time,self.attitude_cmd[:,0])
        ax1[2,0].set_ylabel('phi[rad]')
        ax1[2,1].plot(self.time,self.drone_states[:,7])
        ax1[2,1].plot(self.time,self.attitude_cmd[:,1])
        ax1[2,1].set_ylabel('theta[rad]')
        ax1[2,2].plot(self.time,self.drone_states[:,8])
        ax1[2,2].plot(self.time,self.attitude_cmd[:,2])
        ax1[2,2].set_ylabel('psi[rad]') # 三个姿态角

        self.rate_cmd[-1] = self.rate_cmd[-2]
        ax1[3,0].plot(self.time,self.drone_states[:,9])
        ax1[3,0].plot(self.time,self.rate_cmd[:,0])
        ax1[3,0].set_ylabel('p[rad/s]')
        ax1[3,1].plot(self.time,self.drone_states[:,10])
        ax1[3,1].plot(self.time,self.rate_cmd[:,1])
        ax1[3,0].set_ylabel('q[rad/s]')
        ax1[3,2].plot(self.time,self.drone_states[:,11])
        ax1[3,2].plot(self.time,self.rate_cmd[:,2])
        ax1[3,0].set_ylabel('r[rad/s]') # 三轴角速率

if __name__ == "__main__":
    drone = DroneControlSim()
    drone.run()
    drone.plot_states()
    plt.show()