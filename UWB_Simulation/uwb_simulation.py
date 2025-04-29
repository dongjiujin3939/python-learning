# 验证UWB测距方法
import math
import numpy as np
import matplotlib.pyplot as plt
from LM import LM3DPositioning
from Extend_Kalman_Filter import ExtendKalmanFilter3D

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
        self.z3 = 0.5
        self.location_uwb3 = np.array([self.x3, self.y3, self.z3])
        # uwb节点相对于小车质心的偏移量
        self.uwb1_offset = np.array([self.x1 - self.x0, self.y1 - self.y0, self.z1 - self.z0])
        self.uwb2_offset = np.array([self.x2 - self.x0, self.y2 - self.y0, self.z2 - self.z0])
        self.uwb3_offset = np.array([self.x3 - self.x0, self.y3 - self.y0, self.z3 - self.z0])
        # drone的位置坐标
        self.x_t = 0
        self.y_t = 0
        self.z_t = 0
        self.location_drone = np.array([self.x_t, self.y_t, self.z_t])
        # drone 到三个uwb节点的距离
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        # kalman filter
        self.kf = ExtendKalmanFilter3D(dt = 0.001)
        #记录数据
        self.time_step = []
        self.true_position = []
        self.calculated_position = []
        self.UGV_position = []
        self.filtered_position = []
    
    def Distance_Measured(self, t):
        # uav 地系坐标
        radius = 4
        omega = 0.23
        self.x_t = 5 + radius * math.cos(omega * t)
        self.y_t = 5 + radius * math.sin(omega * t)
        self.z_t = 5.1
        # ugv质心轨迹
        self.x0 = 0.2 + 0.1 * t
        self.y0 = 0.0 + math.sin(0.1 * t)
        self.z0 = 0.1
        self.location_ugv = np.array([self.x0, self.y0, self.z0])
        # 更新后的质心位置
        self.location_uwb1 = self.location_ugv + self.uwb1_offset
        self.location_uwb2 = self.location_ugv + self.uwb2_offset
        self.location_uwb3 = self.location_ugv + self.uwb3_offset
        # 调用LM算法的最小二乘法
        anchors = [
            self.location_uwb1,
            self.location_uwb2,
            self.location_uwb3
        ]

        true_pos = np.array([self.x_t, self.y_t, self.z_t])
        diff = anchors - true_pos
        distances = np.linalg.norm(diff, axis=1)
        # 加入高斯噪声
        noise_std_dev = 0.01
        noise = np.random.normal(0, noise_std_dev, size = distances.shape)
        noisy_distances = distances + noise
        lm = LM3DPositioning(anchors, true_pos)
        # if t == 0:
        #     initial_guess = [0.0, 0.0, 1.0]
        # else:
        #     initial_guess = self.calculated_position[-1]
        initial_guess = [0.0, 0.0, 1.0]
        estimated = lm.levenberg_marquardt(noisy_distances, initial_guess, use_huber = True, delta = 0.3, verbose = True)
        # kalman filter
        if t == 0:
            self.kf.x[:3, 0] = estimated
        self.kf.predict()
        self.kf.update(estimated)
        filtered_estimate = self.kf.get_position()
        # print("Estimated Position:", estimated)
        if t == 199:
            lm.visualize_3d(estimated)

        self.time_step.append(t)
        self.true_position.append((self.x_t, self.y_t, self.z_t))
        self.calculated_position.append(tuple(estimated))
        self.UGV_position.append(self.location_ugv.copy())
        self.filtered_position.append(tuple(filtered_estimate))

    def plot_results(self):
        true_position = np.array(self.true_position)
        calculated_position = np.array(self.calculated_position)
        UGV_position = np.array(self.UGV_position)
        filter_position = np.array(self.filtered_position)
        time_steps = np.array(self.time_step)
        
        position_error = calculated_position - true_position
        error_norm = np.linalg.norm(position_error, axis=1)

        fig = plt.figure(figsize = (16, 8))

        ax1 = fig.add_subplot(121, projection = '3d')
        ax1.plot(true_position[:, 0], true_position[:, 1], true_position[:, 2])
        # ax1.plot(calculated_position[:, 0], calculated_position[:, 1], calculated_position[:, 2])
        ax1.plot(UGV_position[:, 0], UGV_position[:, 1], UGV_position[:, 2])
        ax1.plot(filter_position[:, 0], filter_position[:, 1], filter_position[:, 2], label = 'KF Filtered', color = 'orange')
        ax1.set_title('3D Trajectory of UAV and UGV')
        ax1.set_xlabel('X[m]')
        ax1.set_ylabel('Y[m]')
        ax1.set_zlabel('Z[m]')
        ax1.legend()
        ax1.grid(True)

        ax2 = fig.add_subplot(222)
        ax2.plot(time_steps, position_error[:, 0], label = 'X[error]')
        ax2.plot(time_steps, position_error[:, 1], label = 'Y[error]')
        ax2.plot(time_steps, position_error[:, 2], label = 'Z[error]')
        ax2.set_title(' Three_Axis Position Error')
        ax2.set_xlabel('Time Step')
        ax2.set_ylabel('Error[m]')
        ax2.legend()
        ax2.grid(True)


        ax3 = fig.add_subplot(224)
        ax3.plot(time_steps, error_norm, label = 'Total Position Error(Norm)', color = 'purple')
        ax3.set_title('Position Error Magitude')
        ax3.set_xlabel('Time Step')
        ax3.set_ylabel('Euclidean Error[m]')
        ax3.legend()
        ax3.grid(True)

        plt.tight_layout()
        plt.suptitle("UWB 3D Positioning: True vs Estimated", fontsize = 16, y = 1.02)
        plt.show()

if __name__ == "__main__":
    uwb = Uwb_Simulation()
    for t in range(0, 200):
        uwb.Distance_Measured(t)
    uwb.plot_results()


