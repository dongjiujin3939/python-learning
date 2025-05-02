import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class LM3DPositioning:
    def __init__(self, anchors, true_pos = None):
        self.anchors = anchors
        self.true_pos = true_pos

    def visualize_3d(self, estimated_pos):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection = '3d')

        xs, ys, zs = zip(*self.anchors)

        ax.scatter(xs, ys, zs, c = 'blue', label = 'Anchors', s = 50)
        ax.scatter([self.true_pos[0]], [self.true_pos[1]], [self.true_pos[2]], c = 'red', label = 'True Position', s = 100, marker = 'x')
        ax.scatter([estimated_pos[0]], [estimated_pos[1]], [estimated_pos[2]], c = 'green', label = 'Estimated Position', s = 100, marker = '^')
        ax.plot([self.true_pos[0], estimated_pos[0]], [self.true_pos[1], estimated_pos[1]], [self.true_pos[2], estimated_pos[2]], 'r--', label = 'Error Line')

        ax.set_title('3D Positioning USE LM')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.legend()
        ax.grid(True)
        plt.tight_layout()
        plt.show()

    # 建模 计算测的距离差 和模型的距离差
    def compute_residuals(self, distance, params):
        x, y, z = params
        residuals = []
        for (xi, yi, zi), di in zip(self.anchors, distance): 
            Ri = math.sqrt((x - xi)**2 + (y - yi)**2 + (z - zi)**2)
            residual = Ri - di
            residuals.append(residual)
        return residuals
    # 计算雅可比矩阵
    def compute_jacobian(self, params):
        x, y, z = params
        j = []
        for (xi, yi, zi) in self.anchors:
            dx = x - xi
            dy = y - yi
            dz = z - zi
            Ri = math.sqrt(dx**2 + dy**2 + dz**2)
            if Ri == 0:
                Ri = 1e-8
            j.append([dx/Ri, dy/Ri, dz/Ri])
        return j
    # 矩阵转置
    def transpose(self, mat):
        return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    # 矩阵相乘
    def mat_mul(self, A, B):
        result = [[0.0 for _ in range(len(B[0]))] for _ in range(len(A))] # 初始化结果矩阵
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    # 解线性方程组 Ax = b 高斯消元法
    def  solve_linear(self, A, b):
        n = len(A)
        for i in range(n):
            # 主元选取
            max_row = max(range(i, n), key = lambda r : abs(A[r][i]))
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            # 消元操作
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                b[j] -= factor * b[i]
            # 回带求解
            x = [0.0] * n
            for i in reversed(range(n)):
                x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
        return x
    # huber 损失函数
    def apply_huber_loss(self, residuals, delta = 1.0):
        residuals = np.asarray(residuals, dtype= np.float64)
        abs_r = np.abs(residuals)
        weights = np.where(abs_r <= delta, 1.0, delta / (abs_r + 1e-8))
        return weights
    
    def huber_loss(self, r, delta):
        r = np.asarray(r, dtype = np.float64)
        abs_r = np.abs(r)
        loss = np.where(
            abs_r <= delta,
            0.5 * r**2,
            delta * (abs_r - 0.5 * delta)
        )
        return loss
    # LM算法
    def levenberg_marquardt(self, distance, init_params, max_iter = 1000, lambda_init = 1.0, use_huber = False, delta = 0.1, verbose = False):
        params = init_params[:]
        lambd = lambda_init
        for iteration in range(max_iter):
            residuals = self.compute_residuals(distance, params)

            if use_huber:
                weights = self.apply_huber_loss(residuals, delta)
            else:
                weights = [1.0] * len(residuals)
            
            weighted_residuals = [w * r for w, r in zip(weights, residuals)]

            J = self.compute_jacobian(params)
            for i in range(len(J)):
                for j in range(3):
                    J[i][j] *= weights[i]
            
            JT = self.transpose(J)
            JTJ = self.mat_mul(JT, J)

            for i in range(len(JTJ)):
                JTJ[i][i] += lambd

            JTr = self.mat_mul(JT, [[r] for r in residuals])
            JTr = [row[0] for row in JTr]

            delta_params = self.solve_linear([row[:] for row in JTJ], [-v for v in JTr])
            new_params = [p + d for p, d in zip(params, delta_params)]
            new_residuals = self.compute_residuals(distance, new_params)

            old_error = sum(self.huber_loss(residuals, delta))
            new_error = sum(self.huber_loss(new_residuals, delta))

            if new_error < old_error: # 误差减小接受新参数
                params = new_params
                lambd *= 0.7
            else: # 误差增大拒绝更新
                lambd *= 2.0
            
            if max(abs(d) for d in delta_params) < 1e-8:
                break
            if verbose:
                print(f"Iter {iteration + 1} : params = {params}, error = {new_error: .6f}")
        return params

