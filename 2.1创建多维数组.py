"""
创建多维数组
a.dtype 查看数组数据类型
a.shape 查看一维数组的长度 返回为一个元组(5,)
a.shape[0] 获取一维数组的长度

二维数组
arange(n)只能创建 0 ～ n-1 数组，只能是整数，如果需要元素是其他类型（例如：str等）无法满足
array() 创建数组元素没有类型限制
二维数组，一定是数组嵌套数组
默认元素是字符串
"""


from numpy import *


a = arange(5)
print(a)
print(a.dtype)
print(a.shape )
print(a.shape[0])

m1 = array([arange(3),arange(3),arange(3)])
print(m1)

m2 = array([["a","b",4],
           [1,2,3],
           [2.3,"2.4",90]])
print(m2)
print(m2.shape)  # 输出元组，第一个为行，第二个元素为列
print("{}是{}维数组".format("m2",len(m2.shape)))