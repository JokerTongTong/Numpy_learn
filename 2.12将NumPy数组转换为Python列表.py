# 2.12将NumPy数组转换为Python列表
import numpy as np
'''
NumPy数组转换为Python列表
方法1：tolist
    将NumPy数组转换为Python列表
    一维数组 -> 列表
    二维数组 -> 嵌套列表
方法2：astype
    a.astype(int/str/bool/...)
    将数组a所有元素转换为对应类型(int/str/bool/...)
    返回一个新数组,a不会被修改
'''

# 方法1：tolist
a = np.array([1,2,3,4,5,6])
print("NumPy一维数组a：{}".format(a))
b = a.tolist()
print("Python列表b：{}".format(b))
c = a.reshape(2,3)
print("NumPy二维数组c：\n{}".format(c))
d = c.tolist()
print("Python列表d：{}".format(d))

# 方法2：astype
print(a.astype(str))
print(a)