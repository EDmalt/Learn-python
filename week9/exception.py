# By hefei
"""
@File : exception.py
"""
# 异常处理
# 异常处理标准语法
try:
    num1, num2 = eval(input("请输入两个数"))
    result = num1 / num2
    print(result)
except SyntaxError as ex:
    print("请检查语法")
except ZeroDivisionError as ex:  # 除数不能为0的异常
    print("除数不能为0")
except Exception as ex:  # 所有异常的父类
    print(ex)
else:
    print("没问题")
finally:
    print("不管有没有异常Finally的语句都会被执行")