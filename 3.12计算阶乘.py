# 3.12计算阶乘
import numpy as np


'''
prod() cumprod() 

函数1：prod()  计算一个数的阶乘

函数2：cumprod()  计算一组数的阶乘

'''
a = np.arange(1,11)
print('a',a)
a_res = a.prod()
print('10!',a_res)
a_res1_10 = a.cumprod()
print('1~10阶乘：',a_res1_10)
