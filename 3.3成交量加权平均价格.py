# 3.3成交量加权平均价格
import numpy as np
'''
成交量加权平均价格 VWAP(Volume Weighted Average Price)
    代表金融资产的平均价格
average(price,weights)
    price -> 价格数组
    weights -> 权重数组
    返回加权平均价格
'''
price,weight = np.loadtxt("a.txt",delimiter=",",usecols=(3,4),unpack=True)
vwap = np.average(price,weights=weight)
print("vwap = {}".format(vwap))