# By hefei
#猜数字小游戏
import random
print("猜数字小游戏(0-10):")
num1=random.randint(0,10);#随机
for i in range(5):
    value=eval(input("请输入你猜的数字："))
    #num1=50
    num2=i+1;
    if value==num1:
        print("恭喜你猜对了")
        if num2==1:
            print("您获得了华为mate20——的200元优惠卷一张")
        elif num2>1 or num2<4:
            print("您获得了法拉利——的100元优惠卷一张")
        elif num2==4:
            print("您获得了马尔代夫旅游——的10元优惠卷一张")
        break
    elif value<num1:
        print("小了")
    elif value>num1:
        print("大了")
    print("寄！没猜中")