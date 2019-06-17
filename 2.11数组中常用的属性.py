# 2.11数组中常用的属性
import numpy as np
'''
数组中常用的属性
1.shape 通过元组的形式返回数组每一维度元素的个数
2.dtype 返回数组的元素类型
3.ndim 返回数组的维度
4.size 返回数组元素的总数
5.itemsize 返回数组中的每个元素在内存中所占用的字节数
    数组占用总字节
    1)nbytes属性
    2)itemsize * size 两个属性相乘
6.nbytes 返回数组所有元素一共在内存中所占用的字节数
7.T 返回一个原数组【行|列】转换后的数组
    原数组为二维数组 -- T属性相当于transpose
    原数组为一维数组 -- T属性就是原数组本身
'''


a = np.arange(16).reshape(2,8)
print("原始数组a:\n{}".format(a))

# 1.shape
b = a.shape
print("a.shape:{}".format(b))

# 2.dtype
c = a.dtype
print("a.dtype:{}".format(c))

# 3.ndim
d = a.ndim
print("a.ndim:{}".format(d))

# 4.size
e = a.size
print("a.size:{}".format(e))

# 5.itemsize
f = a.itemsize
print("a.itemsize:{}".format(f))

# 6.nbytes
g = a.nbytes
print("a.nbytes:{}".format(g))
print("a.itemsize*a.size:{}".format(a.itemsize*a.size))

# 7.T
h = np.arange(8).reshape(2,4)
i = np.arange(8)
j = h.T
k = i.T
print("原始二维数组h:\n{}".format(h))
print("二维数组h.T:\n{}".format(j))
print("原始一维数组i:{}".format(i))
print("一维数组i.T:{}".format(k))