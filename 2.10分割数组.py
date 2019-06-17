# 2.10分割数组
import numpy as np
'''
分割数组
1.水平分割 hsplit(数组a,num)
         数组a：被分割的数组 
         num：平均分为几份(num确保a数组的列数可以平均分为num份,否则抛出异常)
    将数组沿着水平方向分割成大小相同的子数组
    a为二维数组，分割后的子数组也为二维数组
2.垂直分割 vsplit(数组a,num)
         数组a：被分割的数组 
         num：平均分为几份(num确保a数组的行数可以平均分为num份,否则抛出异常)
    将数组沿着垂直方向分割成大小相同的子数组
    a为二维数组，分割后的子数组也为二维数组
3.深度分割 b = dsplit(数组a,num)
         数组a：被分割的数组 | np.shape(a) == (3,4,6)
         num：平均分为几份(num确保能被6整除,否则抛出异常)
    将数组沿着深度分割成大小相同的子数组
    a为二维数组，分割后的子数组也为二维数组
    b[0][0] == 第0个平面水平分割第0份(水平按照num分割) 
    b[1][0] == 第0个平面水平分割第1份(水平按照num分割)
    b[0][1] == 第1个平面水平分割第0份(水平按照num分割)
    b[1][1] == 第1个平面水平分割第1份(水平按照num分割)  
    !!! 此处例子数组b为三维数组 !!!  
'''
# 1.水平分割
a = np.arange(16).reshape(4,4)
b = np.hsplit(a,4)
# 2.垂直分割
c = np.vsplit(a,2)
# 3.深度分割
d = np.arange(72).reshape(3,4,6)
e = np.dsplit(d,3)
print("原始数组a:\n{}\n".format(a))
print("水平分割-数组b:\n{}\n".format(b))
print("垂直分割-数组c:\n{}\n".format(c))
print("深度原始数组d:\n{}\n".format(d[1]))
# print("深度分割-数组e:\n{}\n".format(e))
print("深度分割-子数组:\n{}\n".format(e[1][1]))



