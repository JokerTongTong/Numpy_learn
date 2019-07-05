# numpy高级函数

# 4.2获取矩阵主对角线上元素以及计算矩阵的迹
import numpy as np


'''
矩阵的迹(迹数) 矩阵主对角线(左上角->右下角)元素的和

'''

# diagonal:获取主对角线的元素
a = np.array([2,3,4,5,3,5,63,2,3])
a.shape = (3,3)
print(a)
'''
[[ 2  3  4]
 [ 5  3  5]
 [63  2  3]]
'''
print(a.diagonal())  # [2 3 3]


# trace:获取矩阵的迹数
print(a.trace()) # 8