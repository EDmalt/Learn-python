# By hefei
"""
@File : rewrite_reload.py
"""


# 重载--指重载类
# 重写--重写类的方法
# 例如运算符重载
class Myinteger:
    def __init__(self, data=0):
        self.data = data

    def __add__(self, other):
        return Myinteger(self.data * other.data)

    def __str__(self):
        return str(self.data)
