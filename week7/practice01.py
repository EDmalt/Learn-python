# By hefei
# 使用面向对象的方式创建一个圆，分别计算周长和面积
import math
import turtle
import time

class Circle:
    def __init__(self, r):
        self.r = r

    # 圆周长
    def cir(self):
        return 2 * math.pi * self.r

    # 圆面积
    def area(self):
        return pow((math.pi * self.r), 2)


class CircleStandard:
    # 可以先给参数赋默认值
    def __init__(self, r=10, border_color="red", color="blue", x=0, y=0):
        """

        :param r: 半径
        :param border_color: 边框颜色
        :param color: 内部颜色
        :param x: x坐标
        :param y: y坐标
        """
        self.r = r
        self.border_color = border_color
        self.color = color
        self.x = x
        self.y = y

    # 圆周长
    def get_cir(self):
        return 2 * math.pi * self.r

    # 圆面积
    def get_area(self):
        return math.pi * math.pow(self.r, 2)

    # 打印
    def show_v1(self):
        info = "半径为{}的圆周长为{:.2f}\n面积为{:.2f}\n坐标({},{})"
        info = info.format(self.r, self.get_cir(), self.get_area(), self.x, self.y)
        print(info)
        return info

    # 绘画圆
    def show_v2(self):
        global pen
        pen.reset()

        pen.up()  # 抬起笔
        pen.goto(self.x, self.y)  # 移动位置
        pen.down()  # 放下笔
        pen.color(self.border_color)  # 修改边框颜色
        pen.fillcolor(self.color)  # 填充内部颜色
        pen.begin_fill()  # 开始填充
        pen.circle(self.r) # 设置圆半径
        pen.end_fill()

        pen.up()
        pen.goto(-150,-150)
        pen.color("orange")
        pen.write(self.show_v1(),font=("微软雅黑",18)) # 设置字体颜色


if __name__ == '__main__':
    turtle.setup(800,600)
    turtle.title("根据要求画圆")
    pen = turtle.Pen()

    circle = Circle(5)
    print("半径为{}的圆周长为{:.2f}\n面积为{:.2f}".format(circle.r, circle.cir(), circle.area()))
    print("————————————参考答案————————————")
    circle2 = CircleStandard()
    circle2.show_v1()
    circle2.show_v2()

    time.sleep(5)
    circle3=CircleStandard(50)
    circle3.show_v2()

    turtle.done()