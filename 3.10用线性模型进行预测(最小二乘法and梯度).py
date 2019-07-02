# 3.10用线性模型进行预测(最小二乘法、梯度(斜率,导数))
import numpy as np
from datetime import datetime
import matplotlib.pyplot
'''
线性模型：直线方程
    预测就是根据变量求y   二维 -> y=a*x+b
求直线方程
提供一组离散点,通过数学公式计算出一条直线接近离散点,直线就能得到方程

四个离散点,(1,6)(2,5)(3,7)(4,10)

y = b1*x + b2

6 = b1*1 + b2
5 = b1*2 + b2
7 = b1*3 + b2
10 = b1*4 + b2

求f(b1,b2)的最小值
f(b1,b2) = (6-(b1*1+b2))^2 + (5-(b1*2+b2))^2 + (7-(b1*3+b2))^2 + (10-(b1*4+b2))^2
min(f(b1,b2))   最小二乘法
二元函数求偏导
    第一次b1,第二次b2,分别求导,都等于0
    d(f(b1,b2))/d(b1)=0
    d(f(b1,b2))/d(b2)=0
    
    d(f(b1,b2))/d(b1)=20b1+8b2-56=0
    d(f(b1,b2))/d(b2)=60b1+20b2-154=0
    解得:b1=1.4  b2=3.5
代入方程y = b1*x + b2
y = 1.4*x + 3.5
'''
# 用NumPy来实现上述计算
'''
lstsq函数:返回线性矩阵方程的最小二乘法的解
np.linalg.lstsq(a,b,rcond)    其中a,b都为矩阵
a 系数矩阵
    一个二维矩阵
b 结果(y)矩阵
    [6 5 7 10]


'''
x = np.array([1,2,3,4])
y = np.array([6,5,7,10])
a = np.vstack([x,np.ones(len(x))]).T # np.ones(len(x))
                                   # 初始化所有值为1的指定长度的数组|还可以是zeros(len())
''' a 的输出
[[1. 2. 3. 4.]
 [1. 1. 1. 1.]]
 T 之后
 [[1. 1.]
  [2. 1.]
  [3. 1.]
  [4. 1.]]
  第二列,相当于定位初始梯度y=x,然后逐渐递归下降,直到求得导数为0
'''
print(a)
b1,b2 = np.linalg.lstsq(a,y,rcond=None)[0]
print(b1,b2)

matplotlib.pyplot.plot(x,y,'o',label='Point',markersize=15)
matplotlib.pyplot.plot(x,b1 * x + b2, 'b',label='Fitter Line') # 拟合直线
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

'''
dot 计算两个向量的成绩
'''

a1 = np.array([2,3,4])
a2 = np.array([6,7,8])
print(np.dot(a1,a2))