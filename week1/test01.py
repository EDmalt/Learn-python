import turtle


# 自动画圆形
def turtle_01(cir):
    turtle.setup(width=500, height=450)
    while cir > 10 :
        turtle.color("cyan", "purple")
        turtle.pensize(5)
        turtle.speed(5)
        turtle.penup()
        turtle.goto(0, -50)
        turtle.pendown()
        turtle.circle(cir)
        cir -= 10


cir = int(input("请输入圆开始半径："))
turtle_01(cir)
