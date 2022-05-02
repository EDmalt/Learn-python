# By hefei
num1=eval(input("请输入第一种商品数量："))*eval(input("第一件商品价格："))
num2=eval(input("请输入第二种商品数量："))*eval(input("第二件商品价格："))
num3=eval(input("请输入第三种商品数量："))*eval(input("第三件商品价格："))
sumAll=num1+num2+num3
if sumAll>5000:
    print("用户应付：{:.2f}元".format(sumAll*0.7))
else:
    print("用户应付：{:.2f}元".format(sumAll * 0.9))