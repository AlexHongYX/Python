try:
    num = eval(input("请输入一个整数："))
    print("{}的平方为{}".format(num,num**2))
except:
    print("你瞎啊，输入的是整数吗？")
else:
    print("真棒！认真审题了")
finally:
    print("继续努力哦")
