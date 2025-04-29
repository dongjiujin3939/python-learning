import numpy as np

class ExtendKalmanFilter3D:
    def __init__(self, dt, process_noise = 1e-2, measurement_noise = 1e-1):
        self.dt = dt

        self.x = np.zeros((6, 1))

        self.P = np.eye(6) * 2.0 # 状态协方差矩阵
        self.Q = np.eye(6) * process_noise # 过程噪声协方差
        self.R = np.eye(3) * measurement_noise # 测量噪声协方差
    # 状态转移函数
    def state_transition_function(self, x):
        x_pos, y_pos, z_pos, vx, vy, vz = x.flatten()
        dt = self.dt

        vx_new = vx + np.sin(vx * dt)
        vy_new = vy + np.cos(vy * dt)
        vz_new = vz + 0.1 * np.tan(vz * dt)
        # vx_new = vx
        # vy_new = vy
        # vz_new = vz

        x_new = x_pos + vx_new * dt
        y_new = y_pos + vy_new * dt
        z_new = z_pos + vz_new * dt
        
        return np.array([[x_new], [y_new], [z_new], [vx_new], [vy_new], [vz_new]])
    # 观测函数
    def observation_function(self, x):
        return x[:3, :]
    # 状态转移函数的雅可比矩阵
    def jacobian_state_transition(self, x):
        F = np.eye(6)
        dt = self.dt
        vx = x[3, 0]
        vy = x[4, 0]
        vz = x[5, 0]
        F[0, 3] = dt * (1 + dt * np.cos(vx * dt))
        F[1, 4] = dt * (1 - dt * np.sin(vy * dt))
        
        if abs(np.cos(vz * dt)) < 1e-3:
            tan_deriv = .0
        else:
            tan_deriv = dt * 0.1 /(np.cos(vz * dt) ** 2)
        F[2, 5] = dt * (1 + tan_deriv)
        F[3, 3] = 1 + dt * np.cos(vx * dt)
        F[4, 4] = 1 - dt * np.sin(vy * dt)
        F[5, 5] = 1 + tan_deriv
        
        return F
    # 观测函数的雅可比矩阵
    def jacobian_observation(self, x):
        H = np.zeros((3, 6))
        H[0, 0] = 1
        H[1, 1] = 1
        H[2, 2] = 1
        return H
    # 预测
    def predict(self):
        F = self.jacobian_state_transition(self.x)
        self.x = self.state_transition_function(self.x)
        self.P = F @ self.P @ F.T + self.Q
    # 更新
    def update(self, z):
        z = np.reshape(z, (3, 1))
        y = z - self.observation_function(self.x)
        H = self.jacobian_observation(self.x)
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(6) - K @ H) @ self.P
    # 获取估计位置
    def get_position(self):
        return self.x[:3].flatten()

