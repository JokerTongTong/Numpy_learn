# 2.12将NumPy数组转换为Python列表
import numpy as np
'''
NumPy数组转换为Python列表
方法1：tolist
方法2：astype
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