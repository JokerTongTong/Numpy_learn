# 3.2读写CSV文件
import numpy as np
'''
读写CSV文件
CSV文件特征(四种情况)：
    1.纯文本，使用某个字符集，比如ASCII、Unicode、EBCDIC或GB2312；
    2.由记录组成（典型的是每行一条记录）；
    3.每条记录被分隔符分隔为字段（典型分隔符有逗号、分号或制表符；有时分隔符可以包括可选的空格）；
    4.每条记录都有同样的字段序列。
savetxt(fname, X, fmt='%.18e', delimiter=' ') -> 写入
    fname -> 保存后的文件名(如:"a.txt")|(可以是路径[如:../../../a.txt])
    X -> 被保存的数组
    fmt="%.18e" -> 默认为科学计数法
           "%d" -> 整数
         "%.2f" -> 小数点后保留两位数字
           "%s" -> 字符串
    delimiter='' -> 默认空,不分割
             ',' -> 逗号分割
loadtxt(fname, dtype=float, delimiter=None,usecols=None,unpack=False) -> 读取
    fname -> 打开的文件名("a.txt")|(可以是路径[如:../../../a.txt])
    dtype=float -> 默认读取返回float类型
            int -> 返回整型
    delimiter=None -> 分割符默认为空
               "," -> 逗号分割 
    usecols=None -> 默认返回所有列       
         (1,3,4) -> 返回索引为1,3,4三列
    unpack=False -> 默认返回一个NumPy数组
           True -> 拆包返回多个数组分别赋值给左侧变量
    返回一个NumPy数组
'''
a = np.arange(20).reshape(4,5)
print(a)
np.savetxt("a.txt",a,fmt="%d",delimiter=",")
x,y,z = np.loadtxt("a.txt",dtype=int,delimiter=",",usecols=(1,3,4),unpack=True)
print(x,y,z)