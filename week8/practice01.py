# By hefei
"""
@File : practice01.py
"""


def is_chinese(words):
    for char in words:
        if not "\u4e00" <= char <= "\u9fff":
            return False
        else:
            return True


def is_contain_chinese(words):
    for char in words:
        if not "\u4e00" <= char <= "\u9fff":
            return True
        else:
            return False


if __name__ == '__main__':
    print("验证字符串是否为纯中文", is_chinese("中a文"))
