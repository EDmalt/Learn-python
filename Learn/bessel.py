# By hefei
# 定义一个贝塞尔曲线对象
# 练习绘画一个贝塞尔曲线--二次、三次、多次
import math
import turtle

t = 0.0  # 插值控制---区间：[0,1]


# 绘画坐标点
def show(p1, p2, p3, p4):
    global pen
    for i in range(4):
        pnum = "p" + str(i + 1)
        if pnum == "p1":
            pnum = p1
        elif pnum == "p2":
            pnum = p2
        elif pnum == "p3":
            pnum = p3
        else:
            pnum = p4
        pen.up()
        pen.goto(pnum[0] * 100, pnum[1] * 100)
        pen.down()
        pen.fillcolor("black")  # 填充内部颜色
        pen.begin_fill()  # 开始填充
        pen.circle(5)
        pen.end_fill()
        pen.up()
        pen.goto(pnum[0] * 100 + 10, pnum[1] * 100)
        pen.color("red")
        pen.write("p{}:({},{})".format(i + 1, pnum[0], pnum[1]), font=("微软雅黑", 10))  # 设置字体颜色
        i += 1


# 插值公式 i = A + (B - A) * t--A/B为坐标点
def interpolation(a, b):
    x = a[0] + (b[0] - a[0]) * t
    y = a[1] + (b[1] - a[1]) * t
    return [x, y]


class BesselThree:
    # 三次贝塞尔曲线
    def __init__(self, p1=[0, 0], p2=[0, 0], p3=[0, 0], p4=[0, 0], t=0.0):
        """
        :param p1: 坐标1
        :param p2: 坐标2
        :param p3: 坐标3
        :param p4: 坐标4
        :param t:  插值
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.t = t

    # 进行坐标插值
    def besselinterpolation(self):
        # 插值处理--减少到三个坐标
        q1 = interpolation(self.p1, self.p2)
        q2 = interpolation(self.p2, self.p3)
        q3 = interpolation(self.p3, self.p4)

        # 插值处理--减少到两个坐标
        r1 = interpolation(q1, q2)
        r2 = interpolation(q2, q3)

        # 获得最终坐标
        s = interpolation(r1, r2)
        return s


if __name__ == '__main__':
    pass
    p1 = [-2, 0]
    p2 = [0, 2]
    p3 = [0, -2]
    p4 = [2, 0]

    turtle.setup(800, 600)
    turtle.title("贝塞尔曲线")
    pen = turtle.Pen()
    besselthree = BesselThree(p1, p2, p3, p4)
    show(p1, p2, p3, p4)
    while t <= 1:
        besselthree.t = t
        print(besselthree.besselinterpolation())
        pen.down()
        pen.color("black")
        pen.goto(besselthree.besselinterpolation()[0] * 100, besselthree.besselinterpolation()[1] * 100)
        t += 0.1

    turtle.done()
