# By hefei
r=eval(input("请输入圆的半径："))
if r>=0:
    area=3.14*r**2
    print("半径为{:.2f}的圆面积为{:.2f}".format(r,area))
else:
    print("你输入的半径不合法！")