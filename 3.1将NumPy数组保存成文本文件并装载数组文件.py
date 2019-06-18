'''
NumPy常用函数
    1.读写文件的函数
    2.与数组相关的函数
    3.数学与统计分析函数
'''

# 3.1将NumPy数组保存成文本文件并装载数组文件
import numpy as np
'''
将NumPy数组保存成文本文件并装载数组文件
1.savetxt("filename",a,fmt="%d")
    "filename" -> 保存后的文件名(如:"a.txt")|(可以是路径[如:../../../a.txt])
    a -> 被保存的数组
    fmt="%d" -> 指定为整数
                默认为科学计数法
                %.2f 小数点后保留两位
                %s 指定为字符串
2.loadtxt("filename",dtype=int/float/bool/...)
    "filename" -> 打开的文件名("a.txt")|(可以是路径[如:../../../a.txt])
     dtype=int -> 打开后的数组类型
    返回一个NumPy数组
'''
a = np.arange(10).reshape(2,5)
np.savetxt("a.txt",a,fmt="%d")
b = np.loadtxt("a.txt",dtype=float)
print(b)