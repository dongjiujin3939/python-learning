import numpy as np

def euler_method(f, y0, x0, x_end, h):
    # Initialize the solution array
    x = np.arange(x0, x_end+h, h) # 生成数组x，x0起点，x_end+h为终点，h为步长
    y = np.zeros(len(x)) # 指定形状的全零数组 len（x）返回x的长度
    y[0] = y0

    #Euler's Method [By Bottom Science]

    # Iterate over the steps
    for i in range(1, len(x)):
        y[i] = y[i-1] + h*f(x[i-1], y[i-1])

    return x, y

# Define the ODE function
def f(x, y):
    return -y

# Set the initial condition and the step size
y0 = 1
x0 = 0
x_end = 10
h = 0.1

# Solve the ODE
x, y = euler_method(f, y0, x0, x_end, h)

for xx,yy in zip(x,y):
    print("x = ",xx," y = ",yy)