from sympy import* # 引入sympy库中的函数

x = symbols('x') # 创建符号变量x

f = Function('f')
g = Function('g')
y = Function('y') # 创建函数f,g,y

eq1 = f(x).diff(x,2)-2*f(x).diff(x,1)-sin(x)
eq2 = g(x).diff(x,4)-2*g(x).diff(x,3)-5*g(x).diff(x,2)
eq3 = y(x).diff(x,2)-x-sin(x) # 3个高阶微分方程表达式

print('微分方程f(x)的解为',dsolve(eq1,f(x)))
print('微分方程g(x)的解为',dsolve(eq2,g(x)))
print('微分方程y(x)的解为',dsolve(eq3,y(x))) # 求解3个高阶微分方程的解 并打印

