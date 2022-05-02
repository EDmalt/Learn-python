# By hefei
# 函数好处：避免重复代码，组织和简化代码，提高代码可读性

# 自定义一个函数
def print_test(times, text):
    """
    :param times: 打印次数
    :param text: 打印内容
    :return:无返回值
    """
    for i in range(0, times):
        print(text, "{}次".format(i + 1))


# 模拟程序的入口
# if __name__=='__main__'
if __name__ == '__main__':
    print_test(20, "调用函数")

num1=-1234
print("{}绝对值是{}".format(num1,abs(num1)))#abs是求绝对值函数
print("幂运算",pow(2,3))
print("求近似值",round(4.4))#近似值与四舍五入不同，若该数与两边的值一样接近，则选偶数
print("求近似值",round(5.5))

