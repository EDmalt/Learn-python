# By hefei
num1=eval(input("请输入第一个数字："))
type=input("请输入计算方式：")
num2=eval(input("请输入第二个数字："))
if type=="+":
    num3 = num1 + num2
elif type=="-":
    num3 = num1 - num2
elif type=="*":
    num3 = num1 * num2
elif type=="/":
    num3 = num1 / num2
elif type=="%":
    num3 = num1 % num2
else:
    print("该计算方式不存在！")
print("{0}{1}{2}={3}".format(num1,type,num2,num3))