# By hefei

# 计算器
end = "y"
while end == "y" or end == "Y":
    # num1 = eval(input("请输入第一个数字："))
    # operation = input("请输入计算方式：")
    # num2 = eval(input("请输入第二个数字："))
    # if operation == "+":
    #    num3 = num1 + num2
    # elif operation == "-":
    #    num3 = num1 - num2
    # elif operation == "*":
    #    num3 = num1 * num2
    # elif operation == "/":
    #    num3 = num1 / num2
    # elif operation == "%":
    #    num3 = num1 % num2
    # else:print("该计算方式不存在！")
    # print("{0}{1}{2}={3}".format(num1, operation, num2, num3))
    num1 = eval(input("请输入数字1："))
    num2 = eval(input("请输入数字2："))
    operator = input("请输入计算方式：")
    print("{}{}{}={}".format(num1, operator, num2, eval("{}{}{}".format(num1, operator, num2))))
    end = input("是否继续计算？")
