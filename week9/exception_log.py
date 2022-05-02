# By hefei
# @File : exception_log.py

import logging

# 定义日志格式
logging.basicConfig(
    # 异常等级critical>error>warning>info>debug,只记录大于等于当前等级的异常
    level=logging.DEBUG,
    filename="log.log",  # 定义文件名
    filemode="a",  # 定义文件模式 经典: r=读取 w=写入 a=追加
    # 记录内容 asctime是发生时间 line:%(lineno)d:错误行数
    format="-%(asctime)s\n-%(name)s\t-%(filename)s\n[line:%(lineno)d]\n-$(levelname)s\n-%(message)s"
)

try:
    num1, num2 = eval(input("请输入两个数"))
    result = num1 / num2
    print(result)
except SyntaxError as ex:
    print("请检查语法")
    logging.error(ex)
except ZeroDivisionError as ex:  # 除数不能为0的异常
    print("除数不能为0")
    logging.error(ex)
except Exception as ex:  # 所有异常的父类
    print(ex)
    logging.error(ex)
else:
    print("没问题")
finally:
    print("不管有没有异常Finally的语句都会被执行")
