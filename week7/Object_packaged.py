# By hefei
# 隐藏数据域(封装)： 用于保护特殊数据，避免用户直接访问数据。
# 封装方法 ，所有属性私有化private(__)
class Player:
    def __init__(self, name, sex, job, age):
        self.__name = name
        self.__sex = sex
        self.__job = job
        self.__age = age

    # 修改--当不符合规定时修改参数
    def set_age(self, age):
        if 100 < age < 18:
            self.__age = 18
        else:
            self.__age = age

    # 获取参数
    def get_age(self):
        return self.__age


if __name__ == '__main__':
    player = Player("张三", "男", "老板", 31)
    player.set_age(100)  # 只能通过set_age方法修改年龄
    print("张三的年龄是{}".format(player.get_age()))
