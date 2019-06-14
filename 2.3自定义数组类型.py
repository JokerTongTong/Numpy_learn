"""
int8   字节型
int16  短整型
int32  整型
int64  长整型
float32  单精度
float64/float  双精度
bool
str_   字符串类型
"""
from numpy import *

t = dtype([('name',str_,20),('age',int8),('salary',float32),('sex',bool_)])

a = array([('tom',24,5650,1),('roce',18,90000.5,0)],dtype=t)
print(a)
"""
自定义数组类型
将二维数组看做一张表格
1.设定表头，dtype() 
    列表嵌套元组，每个元组控制表格每一列元素
    元组中第一个元素为名字，第二个元素为类型，第三个为长度
2.创建自定义数组array(二维数组,dtype=t)
    二维数组为列表嵌套元组，元组每一项符合dtype设定的类型
"""
