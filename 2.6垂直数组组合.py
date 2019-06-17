from numpy import *
# 垂直组合
'''
垂直组合 vstack((数组a,数组b,数组c))
a,b,c三个数组必须列数一样，如若不一样，会抛出异常,行数无需考虑
'''
a = arange(12).reshape(3,4)
b = arange(16).reshape(4,4)
c = arange(20).reshape(5,4)
d = vstack((a,b,c))

print("数组a:\n{}\n".format(a))
print("数组b:\n{}\n".format(b))
print("数组c:\n{}\n".format(c))
print("组合数组d:\n{}\n".format(d))
# 深度组合