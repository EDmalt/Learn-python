# By hefei
"""
@File : Inheritance_and_polymorphism.py
"""


# 继承与多态
# 继承：方便代码的修改
# 多态：一个类的多种表现形式

# 例子：
# 首先创建父类
class Hero:
    def __init__(self, name, level=1, max_life=100, curr_life=100):
        self.__name = name
        self.__level = level
        self.__max_life = max_life
        self.curr_life = curr_life

    def set_level(self, level):
        if 99 < level < 0:
            level = 1
        self.__level = level

    def get_level(self):
        return self.__level

    def move(self):
        print("父类英雄在行走")

    def __str__(self):
        content = "{}\t{:<4d}\t{:<8d}\t{:<8d}"
        return content.format(self.__name, self.__level, self.__max_life, self.curr_life)


# 定义一个子类
class Warrior(Hero):
    def __init__(self, name, level=1, max_life=100, curr_life=100, physical_attack=50):
        super(Warrior, self).__init__(name, level, max_life, curr_life)  # 继承父类属性初始化方法
        self.__physical_attack = physical_attack

    def __str__(self):
        super(Warrior, self).__str__() + "\t" + str(self.__physical_attack)

    def move(self):
        print("子类战士在移动")


# 定义一个核心类
class Gamecore:
    def move_hero(self, hero):
        hero.move()


if __name__ == '__main__':
    gamecore = Gamecore()
    normal_hero = Hero("普通英雄")
    warrior = Warrior("战士")

    gamecore.move_hero(warrior)
