# 3.5时间加权平均价格
import numpy as np
'''
时间加权平均价格 TWAP(Time Weighted Average Price)
    距离当前时间越近,权重越大
    借用arange()函数产生一个递增的或者递减的数组，代表时间权重t
    average(price,weights=t)
'''
price,weight = np.loadtxt("a.txt",delimiter=",",usecols=(3,4),unpack=True)
t = np.arange(len(price))
twap = np.average(price,weights=t)