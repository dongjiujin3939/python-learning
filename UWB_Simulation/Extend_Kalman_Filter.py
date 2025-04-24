import numpy as np

class ExtendKalmanFilter3D:
    def __init__(self, dt, process_noise = 1e-2, measurement_noise = 1e-1):
        self.dt = dt

        self.x = np.zeros((6, 1))

        self.P = np.eye(6) * 2.0
        self.Q = np.eye(6) * process_noise
        self.R = np.eye(3) * measurement_noise

    def state_transition_function(self, x):
        x_pos, y_pos, z_pos, vx, vy, vz = x.flatten()
        dt = self.dt

        x_new = x_pos + vx * dt
        y_new = y_pos + vy * dt
        z_new = z_pos + vz * dt

        # vx_new = vx + np.sin(vx * dt)
        # vy_new = vy + np.cos(vy * dt)
        # vz_new = vz + 0.1 * np.tan(vz * dt)                    
        vx_new = vx
        vy_new = vy
        vz_new = vz

        return np.array([[x_new], [y_new], [z_new], [vx_new], [vy_new], [vz_new]])
    
    def observation_function(self, x):
        return x[:3, :]

    def jacobian_state_transition(self, x):
        F = np.eye(6)
        dt = self.dt
        vx = x[3, 0]
        vy = x[4, 0]
        vz = x[5, 0]
        F[0, 3] = self.dt
        F[1, 4] = self.dt
        F[2, 5] = self.dt

        F[3, 3] = 1 + dt * np.cos(vx * dt)
        F[4, 4] = 1 - dt * np.sin(vy * dt)
        if abs(np.cos(vz * dt)) < 1e-3:
            F[5, 5] = 1
        else:
            F[5, 5] = 1 + dt / (np.cos(vz * dt) ** 2)
        return F
    
    def jacobian_observation(self, x):
        H = np.zeros((3, 6))
        H[0, 0] = 1
        H[1, 1] = 1
        H[2, 2] = 1
        return H
    
    def predict(self):
        self.x = self.state_transition_function(self.x)
        F = self.jacobian_state_transition(self.x)
        self.P = F @ self.P @ F.T + self.Q

    def update(self, z):
        z = np.reshape(z, (3, 1))
        y = z - self.observation_function(self.x)
        H = self.jacobian_observation(self.x)
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.P = (np.eye(6) - K @ H) @ self.P

    def get_position(self):
        return self.x[:3].flatten()

