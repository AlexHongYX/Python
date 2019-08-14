# 如果一个语句被括号包起来，可以直接跨行书写
# \：换行

# 缩进最好直接打四个空格，而不是Tab键(不同环境下Tab含义不同)

# 多元赋值，同时给多个变量赋值
# x,y = 1,2
# 交换操作
# x = 10
# y = 20
# x,y = y,x
# print(x,y)

# # def会改变变量的作用域
# def func():

#     # 设置文档字符串
#     """
#         this is func
#     """

#     x = 1
#     print("func:",locals())
#     return x

# func()
# print("="*40)
# print("main:",locals())

# # _xxx表示一个“私有变量”，使用from module import *无法导入

# Python内置函数就能查看文档
# # .__doc__：查看文档
# print(func.__doc__)
# # help：查看文档
# help(func)

# type返回的是一个对象，这个对象的类型就是type类型
# Null/None——无意义的值
# def func():
#     x = 10
#     print(x)

# a = func()
# print(a)

# import math
# for i in range(1,10):
#     print(round(math.pi,i))

# 随机种子
# import random
# print(random.randint(1,6))

# # 函数叫做“可调用对象”
# def outer():
#     def inner():
#         print("hehe")
#     inner()

# outer()

# 关键字参数
# def print_point(x=0,y=0,z=0):
#     print(x,y,z)

# print_point(x=100,z=100)

# a = [9,5,2,7]
# b = sorted(a,reverse=True)
# print(a,b)

# # data相当于是一个列表
# def log(*data):
#     for d in data:
#         print(d)

# log(10,30)
# # data相当于是一个元组
# def log(**data):
#     for key in data:
#         print(key,data[key])

# log(x=1,y=2,z=3)

