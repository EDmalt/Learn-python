# By hefei
sumAll=0
num1=eval(input("请输入第一种商品数量："))
discount1=eval(input("第一件商品价格："))
num2=eval(input("请输入第二种商品数量："))
discount2=eval(input("第二件商品价格："))
num3=eval(input("请输入第三种商品数量："))
discount3=eval(input("第三件商品价格："))
sumAll=num1*discount1+num2*discount2+num3*discount3
if discount1>1000 or discount2>1000 or discount3>1000 or sumAll>5000:
    print("用户打七折优惠应付：{:.2f}元".format(sumAll*0.7))
else:
    print("用户应付：{:.2f}元".format(sumAll))