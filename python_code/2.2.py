from sympy import* # 引入sympy中的函数

x = symbols('x') # 创建符号变量x

f = Function('f')
g = Function('g')
y = Function('y') # 创建3个函数 f,g,y

eq1 = diff(f(x),x)-21*f(x)
eq2 = diff(g(x),x)-13*x*g(x)
eq3 = diff(y(x),x)+2*y(x)*tan(x)-sin(2*x) # 3个一阶微分方程的表达式

print('微分方程f(x)的解为',dsolve(eq1,f(x)))
print('微分方程g(x)的解为',dsolve(eq2,g(x)))
print('微分方程y(x)的解为',dsolve(eq3,y(x))) # 求解这3个微分方程 并打印
