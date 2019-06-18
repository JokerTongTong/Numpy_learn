# 3.9根据日期分析股票涨幅
import numpy as np
'''
根据日期分析股票涨幅
涉及函数:
    1)take(a):返回索引对应的值组成的数组
    2)argmax(a):取数组中最大值对应的索引
    3)argmin(a):取数组中最小值对应的索引
'''

# 1)简单收益率
a = np.array([20, 30, 50, 45])
b = np.diff(a) / a[:-1]

# 2)对数收益率
c = np.diff(np.log(a))
d = np.sqrt(a)

# 过滤正数收益率
e = np.where(a)

print(a)
print(b)
print(c)
print(d)
print(e)
print(e[0])