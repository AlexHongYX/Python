# Python中的缩进一定要注意，缩进不对就错了（一般每一级是缩进4个空格）
# Python中的elif是else if的意思（只能写成elif）
# Python并不支持switch-case
# result = input("你愿意敲代码吗？")
# if result == '1':
#     print("offer")
# elif result == '0':
#     print("红薯")
# else:
#     print("输入有误")

# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# # range(start,end)：(start,end]的数据（前闭后开）
# for num in range(1,11):
#     print(num)
# a = [9,5,2,7]
# for num in a:
#     print(num)

# # 打印字典
# a = {'ip':'127.0.0.1','port':80}
# for key in a:
#     print(key, a[key])

# # pass语句：空语句（什么都不做），占位标记
# x = 11
# if x%2 == 0:
#     pass
# else:
#     print("hehe")

# # 列表解析/列表推导
# # 给定一个列表，得到一个新的列表，新的列表中的每个元素都是旧列表的每个元素的乘方
# a = [1,2,3,4]
# b = [x ** 2 for x in a if x % 2 == 1]
# print(b)

# # 函数定义
# # 不用写类型，动态类型（最终类型由运行结果决定）
# def add(x,y):
#     # 函数体
#     ret = x+y
#     return ret
# # Python函数没有重载的规则，同名函数会产生相互覆盖的情况（后面定义的覆盖了前面定义的）
# def add(x,y,z):
#     return x+y+z

# # 函数调用
# ret = add(10,20,30)
# print(ret)

# 函数中支持默认参数值

# # 解包 unpack语法
# # 一个函数可以返回多个值
# def get_point():
#     x = 10
#     y = 20
#     return x,y

# x,y = get_point()
# print(x,y)

# # 不想要x，忽略的用'_'表示就行
# _,y = get_point()
# print(y)

# # 函数返回的实际上是一个元组
# tmp = get_point()
# print(tmp)

# # 函数也是一个对象，可以做返回值/参数，定义别名...
# print(type(get_point))

# 文件操作
# f = open('c:/Users/xiaoaxiao/Desktop/Test.txt','r')

# # 一次读完整个文件的内容，返回了一个列表，列表中的每个元素是文件中的每行数据
# a = f.readlines()
# print(a)

# # 每次读一行
# for line in f:
#     print(line,end='')

# # 写文件
# f = open('c:/Users/xiaoaxiao/Desktop/Test.txt','w')
# f.write('hello world!')
# f.close()

# 统计文本中的词频
# []：key存在则查找，key不存在则插入
# strip：str的方法，功能是去掉字符串头和尾的空白字符（空格，制表符，换行符，垂直制表符，翻页符...）

# import模块：类似Java的包<导入一个模块>
# import calc #不用加.py
# calc.py这个文件必须放在当前目录中，或者系统目录（python安装目录）中——和Java不太相同
# 模块也是一个对象，直接用'.'访问即可
# print(calc.add(10,20))
# 不同模块之间的同名函数相互不影响



