from numpy import *

# reshape(num1,num2,num3)将数组变为多维
# num1 X|num2 Y|num3 Z
a = arange(24)
b = a.reshape(2,3,4)
print("数组a\n{}".format(a))
print("-" * 100)
print("数组b\n{}".format(b))
print("-" * 100)

'''
方法一： revel()
ravel()返回数组的一个视图，修改视图的值，会影响原来的数组
'''
b1 = b.ravel()
b1[0] = 100
print("数组b1\n{}".format(b1))
print("-" * 100)
print("数组b\n{}".format(b))
print("-" * 100)

'''
方法二：flatten()
flatten()会请求新的内存来保存结果，修改并不会影响原来的数组
'''
b2 = b.flatten()
b2[3] = 300
print("数组b2\n{}".format(b2))
print("-" * 100)
print("数组b\n{}".format(b))
print("-" * 100)

'''
方法三：使用元组设置数组的维度 
'''
b.shape = (6,4)
print("数组b\n{}".format(b))
print("-" * 100)

'''
方法四：transpose()
维数转值，行变列列变行
同样返回一个视图，修改视图的值，会改变原数组的值
'''
b3 = b.transpose()
print("数组b3\n{}".format(b3))
print("-" * 100)

'''
方法五：resize()
类似reshape(),resize修改原来的数组，reshape申请新的内存，生成一个新的数组
'''
b.resize(2,12)
print("数组b\n{}".format(b))