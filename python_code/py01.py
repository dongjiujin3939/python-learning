# 打印九九乘法表


# i = 1 #设置列数
# while i <= 9:
#     # print(i)
#     j=1 # 设置行值 
#     while j <= i:
#         # print(f"{i} * {j} = {i*j}",end = "\t") #每内循环一次就输出一次并加上制表符
#         p = i * j   
#         print("%d * %d = %d" % (i,j,p) , end = "\t")
#         j += 1
#     print() # 每结束一次内循环 换行一次
#     i += 1


# 计算从1加到100的和
# s = 0
# for i in range (1,101): 
#     s += i
# print(s)

# replace() 替换

# split() 分割

# capitalize() 首字母大写

# lower() 大写转小写

# upper()  小写转大写

# find() 查找并返回下标值，没有则返回负一

# index() 查找并返回开始位置的下标值，没有则报错

# count() 返回字符串出现次数，没有则返回0

# startwith() 是否以某个字符串开头，是则返回True，否则返回False

# endwith() 是否以某个字符串结尾，是则返回True，否则返回False

# 列表基本操作
# append()  整体添加  extend() 分散添加，逐一添加，必须是可迭代对象  insert() 指定位置插入元素
# del() 删除 pop() 删除指定下标元素，python3默认删除最后一个元素 remve() 根据元素值进行删除 默认删除最先出现的元素
#  sort() 默认从小到大排序 revers() 倒序排序 列表倒置
# 列表推导式 [表达式 for 变量  in 列表]   [表达式 for 变量 in 列表 if 条件]
# 列表嵌套 

# 元组基本操作 只有一个元素，末尾须加上，只能进行查找操作，不支持增删操作

# 字典 字典名 = {键1：值1，键2：值2} 
# 字典中没有下标 查找需根据键名 变量名.get(键名) 没有则返回NONE 可以设置返回默认值
# 修改元素 通过键名修改 键名存在就修改， 不存在则新增
# del 删除整个字典 del 字典名，  键名不存在就报错 clear() 清空整个字典里面的内容，保留字典 pop() 删除指定键值对，键不存在则报错
# len() 求长度 keys() 返回字典里的所有键名 values() 返回字典里面包含的所有值 item() 返回字典里包含的键值对(以元组形式)

# 集合set {} 集合无序，里面的元素唯一 不能修改里面的值 可以根据无序性自动去重
# add 添加整体  update() 添加元素必须是可迭代对象，一个一个传入集合
# remove  选择删除的元素，没有则报错 pop() 对集合进行无序排列，删除左边第一个元素 discard() 选择要删除的元素，没有则无任何改变
# 交集 & 没有共有部分 则返回set() 并集 |  重复的元素不算

#类型转换 int() 转换成整型 float() 转换成浮点型 str() 转换成字符串类型 eval() 执行字符串表达式并返回表达式的值 可实现list dict tuple str 之间的转换
# list ()  将可迭代对象转换成列表  字典转换为列表，取键名组成列表的值 集合转换成列表会先去重再转换

# 深浅拷贝 （只针对可变对象） 赋值：等于完全共享资源，一个值的改变会被另一个值共享,赋值的内存地址是一样的 
# 浅拷贝 copy 数据半共享，会创建新的对象，拷贝第一层的数据，嵌套层会指向原来的内存地址，内存地址不一样
# import copy 
# li = [1,2,3,[4,5]]
# li2 = copy.copy(li)
# print("li",li)
# print("li2",li2)
# print("li的内存地址",id(li)) 
# print("li2的内存地址",id(li2)) # 外存地址不同，内存地址相同 优点 ： 拷贝速度快，占用空间少，拷贝效率高

# 深拷贝 deepcopy 数据完全不共享，外层对象和内部元素都拷贝一遍

# 可变类型 变量对应的值可以修改，但内存地址不会改变 dict list set 
# 不可变对象 存储空间保存的值不能被修改 整形 字符串 元组 

# 函数 结构 
# def 函数名()：
#     函数体
# 调用函数 函数名()
# 返回值 return  会给函数的执行者 返回值
# 函数中有return 则代表函数运行结束，不继续执行 return 返回多个值，则以元组的形式返回调用者 无返回值则返回none
# return 返回计算结果，print则是打印结果

# 参数 结构
# def 函数名(形参a，形参b)：
# 函数体
# ...（如a=1,b=2)
# 调用格式
# 函数名（实参1，实参2） 

# 默认参数 为参数提供默认值，调用函数时可不传该默认参数的值
# def fun(a = 12):     所有位置参数必须出现在默认参数之前，包括函数定义和调用

# 可变参数 传入的值的数量是可变的，可以传多个，也可不传
# 格式 def func(*args) 以元组形式接收 

# 关键字参数 
# def func(**kwargs) 以字典形式接收  传值需要键 =值的形式

# 函数嵌套 在一个函数 里面调用另一个函数
# 嵌套定义  在一个函数中定义另一个函数  

# 作用域  变量生效的范围，全局变量和局部变量
# 全局变量 函数外部定义的变量 在整个文件中都有效
# 局部变量 函数内部定义的变量，从定义位置开始，到函数定义结束位置有效  只能在被定义的 函数中使用
# 在函数内部 修改全局变量的值，global关键字
# global 将变量声明为全局变量  格式 gloal 变量名
# nonlocal 用来声明外层的局部变量，只能在嵌套函数中使用，在外部函数先进行声明，内部函数进行nonlocal声明 nonlocal只能对上一级进行修改

# 匿名函数 函数名 = lambda 形参 ： 返回值（表达式） 调用： 结果 = 函数名（实参）  
# lambda的参数形式 无参数， 一个参数， 默认参数 （默认参数必须在非默认参数后面）关键字参数
# lambda 结合if条件判断 只能实现简单逻辑

# 内置函数  查看所有的内置函数
# import builtins
# print(dir(builtins))   大写字母开头一般是内置常量名，小写字母开头一般是内置函数名
# abs() 返回绝对值
# sum() 求和 放可迭代对象
# min() 求最小值
# max() 求最大值
# print(min(-8,5,key = abs)) 传入绝对值函数

# zip() 将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# li = [1,2,3]
# li2 = ['a','b','c']
# print (zip(li,li2))
# 第一种方法取出元素
# for i in zip(li,li2):
#     print(i)
#     print(type(i)) # 元素取出一一对应
# 第二种方式，转换成列表打印
# print (list(zip(li,li2))) # 必须是可迭代对象

# map()  可以对可迭代对象中每一个元素进行映射，分别执行
# map(func,iterl) # func 自己定义的函数 iterl 要放进去的可迭代对象
# 对象中每个元素都会执行这个函数
# li = [2,3,4]
# def func(x):
#     return  x * 6
# mp = map(func,li)
# print (mp)
# 第一种 for循环取出
# for i in mp:
#     print (i)
# 第二种 转换成列表
# print (list(map(func,li)))

# reduce() 先把对象中的两元素取出，计算出一个值然后保存，再把这个值与第三个元素进行计算
# from functools import reduce
# reduce (function,sequence) function 函数，必须有连个参数的函数，sequence 序列 可迭代对象
# li2 = [1,2,3,4]
# def add(x,y):
#     return x + y
# res = reduce(add,li2)
# print(res)

# 拆包 对于函数中的多个返回数据，去掉元组，列表或者字典，直接获取里面数据的过程
# tua = (1,2,3,4)
# print(tua)
# print(tua[0])
# 方法1
# a,b,c,d = tua 
# print(a,b,c,d)
# 元组内的元素要与接收的变量个数相同
#方法2
# a,*b = tua    第一个元素给a，其余的所有给b
# print(a,b)
# 一般在函数调用时使用

# 异常
# 异常处理 根据错误信息修正 traceback：追踪 XXXerror ：异常类型，包含异常具体信息
# 对异常进行捕获处理     
# 方法1 
# try：
#     不确定是否能够正常执行的代码
# except Exception as e:           Exception 万能异常  as 相当于取别名，e是变量名，as e 相当于把异常信息保存到变量e中
#     如果检测到异常，就执行这个位置的代码

# 方法2
# try: 
#     可能会引发异常的代码
# except:
#        出现异常的处理代码
# else:
#       没有捕获到异常执行的代码    try和else一起执行

# 方法3
# try:
#     可能会引发异常的代码
# except:
#     出现异常的处理代码
# else:
#     未出现异常的处理代码
# finally:
#     try代码块结束后运行的代码(表示无论是否检测到异常，都会执行)
# try...finally...可单独使用

# 抛出异常 rasie
# 步骤:
# 1 创建一个Exception("xxx")对象，xxx--异常提示信息
# 2 rasie抛出这个对象(异常对象)
# def funca():
#     raise Exception("error")
#     print("666") # 执行了raise语法，代码不会继续运行
# funca()

# def login():
#     pwd = input("please input your password：")
#     if len(pwd) >= 6:
#         return "input successful"
#     raise Exception("length error! plese input agin")
# print(login())

# try:
#     print(login())
# except Exception as e:
#     print(e)

# 模块 导入一个模块本质上就是执行一个py文件
# 内置模块 random time os logging 直接导入就能使用
# 第三方库 需要下载
# 自定义模块 自己定义的模块

# import导入模块 用法： import 模块名
# 调用功能： 模块名.功能名
# import pytest
# print(pytest.name)

# 从模块中导入指定的部分 from 模块名 import 功能1，功能2  调用功能1,2不需要模块名
# from pytest import func
# func()

# from 模块名 import *  把模块中的所有内容全部导入 不建议使用
# from pytest import *
# func()
# funa()

# as 给模块起别名 import 模块名 as 别名
# 给功能起别名  from 模块名 import 功能 as 别名
# import pytest as pt
# pt.func()

# 内置全局变量 __name__ 语法： if __name__ == "__main__"  用来控制py文件在不同的应用场景执行不同的逻辑
# 1.文件在当前程序执行（自己执行自己）： __name__ == "__main__"
# 2.文件被当做模块被其他文件导入：__name__ == 模块名 被当做模块导入时下面的代码不会显示出来

# 包 就是项目结构中的文件夹或目录 包是含有__init__.py文件
# 将有联系的模块放到同一个文件夹下，可以有效避免模块名称冲突的问题，让结构更加清晰