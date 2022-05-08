# By hefei
# @File : numpy_and_list.py

import numpy  # 导入numpy库


# 对比原生python-list对数组操作的方式

# 原生list数组的创建
def python_list(n):
    a = [pow(i, 2) for i in range(n)]  # 创建n的次方数组
    b = [pow(i, 3) for i in range(n)]  # 创建n的立方数组
    c = []  # 创建一个第三方数组用于保存操作后的结果
    # 相加两个数组
    for i in range(n):
        c.append(a[i] + b[i])
    return c


# 使用numpy来创建数组
"""
    1.arange与list的range是一样的
"""


def python_numpy(n):
    a = pow(numpy.arange(n), 2)  # 创建n的次方数组
    b = pow(numpy.arange(n), 3)  # 创建n的立方数组
    return a + b


if __name__ == '__main__':
    print("原生list创建的两个数组和：{}\nnumpy创建的数组和：{}".format(python_list(4), python_numpy(4)))

    """
        numpy的array对象，
        shape:返回一个元组，表示array的维度
        ndim：返回一个数字，表示array的维度数目
        size：返回一个数字，表示array的元素数目
        dtype：返回array中元素的数据类型
    """
    # numpy.ones(shape,dtype=None,order=‘C')用于创建全是1的数组
    """
        其他相同的方法有zeros /empty等，其中empty虽然默认值都为0，但是值并未初始化，不可直接调用
        其中shape是用于定义数组类型的，用于决定数组是几维的数组，shape=n时就是一个n位数的一维数组
        shape=(n,m)时就是一个n行，m列的二维数组，以此类推
    """
    one_dimensional = numpy.ones(10)
    two_dimensional = numpy.ones((2, 3))
    print("ones创建一维数组：{}\nones创建二维数组：{}".format(one_dimensional, two_dimensional))

    # 使用full创建指定值的多维数组，语法：numpy.full(shape,value,dtype,order)
    full_one = numpy.full(10, 233)
    full_two = numpy.full((2, 3), 332)
    print("一维的值为233的数组{}\n二维的值为332的数组{}".format(full_one, full_two))

    # 使用random模块来创建随机数的数组
    # randn(d1,d2,d3……,dn)参数是用于定义创建几维的数组

    randn1 = numpy.random.randn()  # 一维一位随机数的数组
    randn1_3 = numpy.random.randn(3)  # 一维三位随机数的数组
    randn2 = numpy.random.randn(2, 3)  # 二维随机数数组
    randn3 = numpy.random.randn(2, 3, 4)  # 三维随机数数组

    print("一维{}\n一维3位数{}\n二维{}\n三维{}".format(randn1, randn1_3, randn2, randn3))

    array_test = numpy.arange(10).reshape(2, 5)  # 创建一个一维数组并转换为二维数组
    print("查看数组类型：", array_test.shape)
    print("原数组{}\n数组元素+1：{}".format(array_test, array_test + 1))
    print("数组元素*3", array_test * 3)
    print("求数组元素的sin函数", numpy.sin(array_test))
    print("求e的数组元素次方", numpy.exp(array_test))

    print("矩阵与矩阵运算")
    array_test2 = numpy.random.randn(2, 5)
    print("矩阵1+矩阵2", array_test + array_test2)

    # numpy索引查询，与原版list差不多
    array_1 = numpy.arange(10)
    array_2 = numpy.arange(20).reshape(4, 5)
    # 二维数组索引查询
    print("原数组:", array_2)
    # x[行][列]
    print("第一行第三列的值", array_2[1][3])
    print("查询第二行的所有列", array_2[2])
    print("切片", array_2[:2, 2:4])
    # 神奇索引--可直接通过值来找到数组中对应的值
    print("一维数组的神奇索引", array_1[[5, 9]])
    indexs = numpy.array([[0, 2], [1, 3]])
    print("将array1的对应值取出并放到新数组内", array_1[indexs])

    # 布尔索引
    print("筛选所有大于5的数", array_1[array_1 > 5])
    for i in range(10):
        print()

    a=numpy.array([[1,2],[3,4]])
    b=numpy.array([[4,5],[6,7]])
    print(numpy.vdot(a,b,))