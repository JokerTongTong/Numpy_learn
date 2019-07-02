# 3.11对数组的修剪和压缩
import numpy as np


'''
clip  compress

修剪数组
a = clip(设定的最小值，设定的最大值)  --  返回一个新数组，且不改变原来数组
数组的修剪：
    将所有比给定最大值还大的数组值都设为给定的最大值
    将所有比给定最小值还小的数组值都设为给定的最小值

压缩数组
a = compress(数组>4)
    括号中为条件，数组+比较符号+数值
    返回一个新数组，且不改变原来的数组

'''

a = np.arange(10)
print('a',a)
print('clipped',a.clip(3,5))
print(a)

print('Compressed',a.compress(a>4))
print(a)