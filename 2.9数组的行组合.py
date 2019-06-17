# 2.9数组的行组合
import numpy as np
'''
数组的行组合 -- 将多个相同长度的一维数组按照行方向组合
row_stack((数组a,数组b,数组c))
组合后a数组为二维数组的第一行,b数组为二维数组的第二行,c数组为二维数组的第三行
a,b,c三个一维数组长度一样，如若不一样，会抛出异常

如若操作二维数组
a,b,c三个一维数组列数一样，如若不一样，会抛出异常，行数无需考虑
与垂直组合效果,完全一样
'''
a = np.arange(5)
b = np.array([0,11,22,33,44])
c = np.array([0,111,222,333,444])
d = np.row_stack((a,b,c))
print("数组a:\n{}\n".format(a))
print("数组b:\n{}\n".format(b))
print("数组c:\n{}\n".format(c))
print("数组d:\n{}\n".format(d))
print(np.shape(d))
print('-'*50)
aa = np.arange(6).reshape(2,3)
bb = np.array([[ 0,11,22],
               [33,44,55]])
cc = np.array([[  0,111,222],
               [333,444,555],
               [333,444,555]])
dd = np.row_stack((aa,bb,cc))
print("数组aa:\n{}\n".format(aa))
print("数组bb:\n{}\n".format(bb))
print("数组cc:\n{}\n".format(cc))
print("数组dd:\n{}\n".format(dd))
print(np.shape(dd))


