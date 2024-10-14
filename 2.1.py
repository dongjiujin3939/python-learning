from sympy import * # 引入sympy中的函数

a,x = symbols('a x') # 创建两个符号变量 a,x

y = x**2+3*x+2
z = x**4-1
u = x**2-2*a*x+a**2 # 3个线性方程表达式

print(y)
print(z)
print(u) # 打印这3个线性方程

x1 = solve(y,x)
x2 = solve(z,x)
x3 = solve(u,x) # 使用solve函数分别求解这3个线性方程

print("方程1的解x1为",x1)
print("方程2的解x2为",x2)
print("方程3的解x3为",x3) # 打印求解的线性方程的解