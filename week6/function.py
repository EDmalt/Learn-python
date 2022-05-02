# By hefei
num_int = int()  # 转换成int类型
num_float = float()  # 转换成float类型
num_bool = bool()  # 转换成布尔类型，默认为false

# 复数有实部和虚部，运算就是实部加实部，虚部加虚部
num1 = complex("4+5j")
num2 = complex(3, 4)
print(num1 + num2)

# ASCII码转换函数
print("空格的ASCII码是", ord(" "))  # 将字符转换成ASCII码
print("ASCII 65代表字符", chr(65))  # 将ASCII码转换字符

# Math模块
import math  # 要导包，一般放在文件开头，这做学习使用放在这里

print("对浮点数取绝对值", math.fabs(-14.33))
print("向上取整", math.ceil(3.4))  # 相当于进1
print("向下取整", math.floor(3.9))  # 相当于去尾

# 求三角形各角弧度及角度练习
x1, y1 = 90, 100  # 一个顶点的坐标
x2, y2 = 205, 85
x3, y3 = 310, 240
# 求三边长度
a = math.sqrt(pow((x2 - x3), 2) + pow((y2 - y3), 2))  # sqrt函数是返回数字的平方根，就是开平方
b = math.sqrt(pow((x1 - x3), 2) + pow((y1 - y3), 2))
c = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
print("三角形三边长度分别为a边{:.2f}\tb边{:.2f}\tc边{:.2f}".format(a, b, c))
# 求角的弧度以及角度
A = math.acos((a * a - b * b - c * c) / (-2 * b * c))  # acos函数是返回数字反余弦
print("角A对应弧度为{:.2f},角度为{:.2f}".format(A, math.degrees(A)))  # degrees函数是弧度转角度
B = math.acos((b * b - a * a - c * c) / (-2 * a * c))
print("角B对应弧度为{:.2f},角度为{:.2f}".format(B, math.degrees(B)))
C = math.acos((c * c - b * b - a * a) / (-2 * a * b))
print("角C对应弧度为{:.2f},角度为{:.2f}".format(C, math.degrees(C)))
# 根据海伦公式计算三角面积S=根号p*(p-a)*(p-b)*(p-c) p为半周长
C=a+b+c # 三角形周长
p=C/2 # 三角形半周长
S=math.sqrt(p*(p-a)*(p-b)*(p-c)) # 海伦公式
print("根据海伦公式算出三角形的面积为{:.2f}".format(S))

