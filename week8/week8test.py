# By hefei
"""
@File : week8test.py
"""


class Login:
    def __init__(self, name="", password=""):
        self.__name = name
        self.__password = password

    def set_name(self, name: str):
        # 可以单独设定一个非法字符串集来规定
        invalid_chars = "!@#$%^&*()+=<>?"
        chars_tf = False
        for char in name:
            if char not in invalid_chars:
                chars_tf = True
            else:
                chars_tf = False

        if 25 < len(name) <= 0 or not chars_tf:
            print("输入的姓名不合法")
        else:
            self.__name = name

    def set_password(self, password: str):
        # 构建所有有效字符
        value_letter = [chr(value) for value in range(ord("A"), ord("Z") + 1)]
        value_letter += [chr(value) for value in range(ord("a"), ord("z") + 1)]
        value_letter += [chr(value) for value in range(ord("0"), ord("9") + 1)]
        value_letter += ["_@#$!"]

        # 验证密码
        if 18 < len(password) < 6:
            return False
        # 如果value_letter定义在函数外就要用global来定义为全局变量
        for char in password:
            if char not in value_letter:
                return False
        self.__password = password
        if password.isdecimal() or password.isalpha():
            return "▲" * 2
        elif password.isalnum() or isnumandsymbol(password):
            return "▲" * 4


def isnumandsymbol(password):
    valid_symbols = [chr(value) for value in range(ord("0"), ord("9") + 1)]
    valid_symbols += ["_@#$!"]
    valid_symbols = str(valid_symbols)  # 转换类型
    for char in password:
        # find是字符串中查找字符的下标，没有字符则返回-1
        if valid_symbols.find(char) == -1:
            return False
    return True


def isletterandsymbol(password):
    pass


if __name__ == '__main__':
    login = Login()
    login.set_name("asdadsa")
    login.set_password("22sdadsd")
