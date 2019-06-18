# 3.6寻找最大值和最小值以及计算数组的取之范围
import numpy as np
'''
寻找最大值和最小值以及计算数组的取之范围
max(a)
    返回数组a中的最大值
min(a)
    返回数组a中的最小值
ptp(a)
    返回数组a的范围 等同于 max(a)-min(a)
'''
h,l = np.loadtxt("a.txt",delimiter=",",usecols=(4,5),unpack=True)
max_num = np.max(h)
min_num = np.min(l)
fanwei = np.ptp(h)
print(max_num)
print(min_num)
print("数组h的范围={}".format(fanwei))