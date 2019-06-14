from numpy import *

# 水平组合
'''
水平组合
行行拼接
两个数组 A|B  A和B水平组合
A行和B行相加
'''
a = arange(12).reshape(3,4)
b = a * 3
c = hstack((a,b))    # hstack()可以将多个数组水平组合，此处例子为两个数组水平组合，
'''
hstack()，参数传入元组；
可以将多个数组水平组合，此处例子为两个数组水平组合
数组水平组合可以任意多个，但是必须行数相同，否则会抛出异常
'''
print("a数组\n{}".format(a))
print("="*20)
print("b数组\n{}".format(b))
print("="*20)
print("c数组\n{}".format(c))
print("="*20)
# 垂直组合
# 深度组合