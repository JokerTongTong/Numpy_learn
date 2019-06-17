import numpy as np
# 深度组合
'''
深度组合 -- 多个相同行相同列数的二维数组组合；每个数组的每个元素组合为一个一维数组
深度数组组合 dstack((数组a,数组b,数组c))
a,b,c三个数组必须行|列数分别一样，如若不一样，会抛出异常
'''
a = np.arange(10).reshape(2,5)
b = np.array([[0,11,22,33,44],
           [55,66,77,88,99]])
c = np.array([[0,111,222,333,444],
           [555,666,777,888,999]])
d = np.array([[0,1111,2222,3333,4444],
           [5555,6666,7777,8888,9999]])
ee = np.dstack((a,b))
eee = np.dstack((a,b,c))
eeee = np.dstack((a,b,c,d))
print("数组a:\n{}\n".format(a))
print("数组b:\n{}\n".format(b))
print("数组c:\n{}\n".format(c))
print("数组d:\n{}\n".format(d))
print("组合数组ee:\n{}\n".format(ee))
print(ee.shape)
print("组合数组eee:\n{}\n".format(eee))
print(eee.shape)
print("组合数组eeee:\n{}\n".format(eeee))
print(eeee.shape)
print(eeee[0][0])
print(eeee[0][1])
print(eeee[0][2])
print(eeee[1][3])

