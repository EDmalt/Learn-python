# By hefei
# 函数自定义
def get_sum(start, end):
    """
    :param start: 开始值
    :param end: 终止值
    :return:无
    """
    if start > end:
        start, end = end, start
    result = 0
    for i in range(start, end + 1):
        result += i
    return result


def level(num):
    """

    :param num:传入积分参数
    :return:
    """
    str_level = ""
    if 80 <= num < 90:
        str_level = "青铜"
    elif 90 <= num < 100:
        str_level = "白银"
    elif 100 <= num:
        str_level = "黄金"
    else:
        str_level = "不合法"
    return str_level


def print_words(words, count):
    for i in range(count):
        print(words)


if __name__ == '__main__':
    print(get_sum(100, 0))
    print(level(eval(input("请输入积分:"))))

    # 函数传参数有几种，一种位置传参，一种关键字传参
    # 位置传参---按照参数所在顺序一对一传参,顺序不能改变
    print_words("abc", 5)
    # 关键字传参---可以改变顺序，只要写明参数关键字
    print_words(count=5, words="ass")
    # 混合传参---位置传参不能放在关键字传参后面且字符串类型要与所在位置参数对应
    print_words("acc",count=5)
