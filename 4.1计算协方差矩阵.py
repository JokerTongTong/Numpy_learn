# numpy高级函数

# 4.1计算协方差矩阵
import numpy as np


'''
Cov(X,Y)=E(X-E(X))(Y-E(Y))
X,Y为两个向量；计算这两个向量的协方差矩阵;等号右侧为计算公式
向量两个,计算出来的矩阵就是 2*2 的矩阵
所以就有4个矩阵元素

'''
a = np.array([1,3,4,5])
b = np.array([2,6,2,2])
x = np.vstack((a,b))
res = np.cov(x)

# cov函数会将正常结果缩小到原来的三分之一

print(x)
print(res)


