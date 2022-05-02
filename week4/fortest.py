# By hefei

#range()看起来是函数 其实是个类 他返回的是一个可迭代得对象 其实就是一个列表[]
# range(x,y,z)x是起始位置，y是结束位置，z是步长，也就是一次加多少
total=0
count=0
for i in range(10):
    num=eval(input("请输入成绩："))
    if num<0:
        print("输入值有误！")
        break#循环一般可以使用break中断循环
    total+=num
    count+=1
print("全班总分{}，平均分{}".format(total,total/count))

