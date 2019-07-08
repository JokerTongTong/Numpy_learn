import numpy as np
'''
transpose(a,b) 不传参数默认全部颠倒轴，传入参数根据转入轴的顺序进行位置变换
a 为numpy数组
b 为数组a所有轴变换后的顺序元组形式
例如：
    c = np.transpose(a,(0,1,3,2,4))
'''
'''
swapaxes(a,b,c)  b/c轴互换位置 
a 为numpy数组
b 为数组轴
c 为数组轴
'''
a = np.arange(32).reshape(2,2,2,2,2)
# print('a{}'.format(a) + '\n--------------------------------')
# print(a[0,1,0,1,1])
# b = a.transpose((0,1,3,2,4))
# print('修改前a[0,1,0,1,1]=',a[0,1,0,1,1],'---------')
# b[0,1,1,0,1] = 1111
# print('修改后a[0,1,0,1,1]=',a[0,1,0,1,1],'---------')
# print(b[0,1,1,0,1])
# print('b{}'.format(b) + '\n--------------------------------')
# print('a{}'.format(a) + '\n--------------------------------')
c = np.swapaxes(a,0,4)
# c = np.transpose(a,(0,1,3,2,4))
print(c)






