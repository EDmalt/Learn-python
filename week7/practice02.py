# By hefei
import time


class Player:
    def __init__(self, id, name):
        """

        :param id: 游戏id
        :param name: 人物名称
        :param level: 等级
        :param vip: vip等级
        :param value_of_diamond:充值的钻石
        :param __money:  充值金额
        """
        self.__id = id
        self.__name = name
        self.__level = 1
        self.__vip = 0
        self.__value_of_diamond = 0
        self.__money = 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_vip(self):
        return self.__vip

    # 充钱
    def recharge(self, money):
        if money < 1:
            print("sorry,最低金额为1元")
            return
        self.__money += money
        self.__value_of_diamond += money * 100
        self.update_vip()

    # 更新vip等级
    def update_vip(self):
        # 通过遍历数组的方式来进行vip增加判断
        money_value = [10, 50, 100, 300, 1000, 2000, 10000, 20000]
        for i in range(len(money_value)):
            if self.__money >= money_value[i]:
                self.__vip = i + 1

    # 魔术方法：不需要调用，满足条件自动调用
    def __str__(self):
        # 需要返回字符串时自动调用
        countent = "游戏ID：{}\t角色名：{}\nvip等级=V{}\t已充值：{}"
        return countent.format(self.__id, self.__name, self.__vip, self.__money)


if __name__ == '__main__':
    player = Player(114514, "野兽战神")
    for i in range(50):
        player.recharge(50)
        print(player)
        print("=" * 50)
        time.sleep(1)
