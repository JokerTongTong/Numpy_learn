# 3.9根据日期分析股票涨幅
import numpy as np
from datetime import datetime
'''
根据日期分析股票涨幅
涉及函数:
    1)take(a):返回索引对应的值组成的数组
    2)argmax(a):取数组中最大值对应的索引
    3)argmin(a):取数组中最小值对应的索引
'''


def datestr2num(time):
    return datetime.strptime(time.decode('utf-8'),'%d-%m-%Y').date().weekday()


data,b = np.loadtxt('data.csv',delimiter=',',usecols=(1,6),unpack=True
                 ,converters={1:datestr2num})

# data数组进行强制类型转换,元组中的每个元素都转换为int类型
data = data.astype(int)


'''
'data.csv' -> filebath
delimiter -> 分割符
usecols=(1,6) -> 要操作的列的索引,元组的形式,可以多列(0,1,2,3,4,5)
unpack=True -> 拆包 默认False
converters={1:datestr2num} -> 参数为字典,key是要转换的列的【索引】,
                                       value是转换用的函数名
'''