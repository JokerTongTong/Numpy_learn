# 3.7计算数组的中位数和方差
import numpy as np
'''
计算数组的中位数和方差
1.中位数 median(a)
    返回数组a的中位数
2.数组排序 msort(a) 
    对数组a升序排序
    返回排序后的数组
3.方差var(a)
    返回数组a的方差
'''
a = np.array([1,3,6,2,12,43,23,12,13,20,90,78,54])
b = np.median(a)
c = np.msort(a)
d = np.var(a)
print(a)
print(b)
print(c)
print(d)