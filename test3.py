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
