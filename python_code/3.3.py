class PID_Controller:
    # 给pid的三个参数赋初值
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0.0
        self.integral = 0.0

    def change_para(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def control_action(self, error, dt):
        """
        Args:
            error: 当前误差
            dt: 步长

        Returns: pid的输出
        """
        p = self.kp * error

        self.integral += error # 将self.integral的值加上当前的error值再重新赋给 self.integral
        i = self.ki * self.integral # 积分控制的本质就是误差的累加

        derivative = (error - self.last_error) / dt
        d = self.kd * derivative # 微分控制的本质就是误差的变化率
        self.last_error = error # 将当前的误差赋给之前的误差

        return p + i + d


import numpy as np


class levitationSys:
    def __init__(self, ncount, x10, x20, y10, y20):
        self.x10 = x10
        self.x20 = x20
        self.X1 = np.zeros(ncount)

        self.y10 = y10
        self.y20 = y20
        self.Y1 = np.zeros(ncount)
        self.Y2 = np.zeros(ncount)

    def system_io(self, i, input, h, f):
 
        y1 = self.y10 + h * self.y20
        y2 = self.y20 + h * (-4900 * self.y10 + 3.1877 * input);.03
        self.Y1[i] = self.y10
        self.Y2[i] = self.y20

        self.y10 = y1
        self.y20 = y2

        return y1


