"""
arange(n)
创建一个NumPy数组 [0 1 2 3 4 ... n-1]

arange(n) ** 2
NumPy数组每个元素平方运算
"""



from numpy import arange


def sum(n):
    a = arange(n) ** 2
    b = arange(n) ** 4
    c = a + b
    return c



if __name__ == '__main__':
    print(sum(5))
