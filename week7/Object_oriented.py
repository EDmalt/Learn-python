# By hefei
# 面向对象就是对事物的抽象，是编程的一种指导思想，规范编程过程，一种全新的组织代码的方式，是更加符合人类的思维
# 使用面向对象描述世界的方法--1，发现类；2，找特征(属性)；3，找出行为(方法/函数)。
# 数据抽象：是状态和行为的结合
# 类就是对象的抽象
# __xxx__这种命名的方法叫魔术方法；特点是不用调用，会在符合条件时自动调用
class Actor:
    # 创建并初始化属性
    def __init__(self, name, sex, job, level):
        # 相当于java中的this.xxx=xxx
        self.name = name
        self.sex = sex
        self.job = job
        self.level = level

    def perfrom(self):
        print(self.name, "正在表演才艺")

    def run(self):
        pass  # 占位符


if __name__ == '__main__':
    actor = Actor("张三", "男", "小丑", 7)
    actor.name="女是"
    print(actor.name)
    actor.perfrom()  # 调用对象的某个函数
