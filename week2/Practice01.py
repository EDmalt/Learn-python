# By hefei
# 算法练习：德雷克公式
# 公式：N=Ng×Fp×Ne×Fl×Fi×Fc×FL

Ng=24183300 #某城市人口
Boy,girl=12323000,1187500#男女生人数
Fp=girl/Ng# 女生人数占比

Ne=(girl-15000*Fp)/girl# 适合的女生占比
Fl=20/100/2

Fi=232323/Ng
Fc=0.05
l=0.1
N = Ng*Fp*Ne*Fl*Fi*Fc*l
print(N)

# 整钱兑换零钱
money=eval(input("请输入金额："))
money_int=int(money)# 获取整数部分
money_float=int(money*10%10)# 获取小数部分
print("十元纸币：",money_int//10,"张")
print("五元纸币：",money_int%10//5,"张")
print("一元纸币：",money_int%10%5,"张")
print("五角硬币：",money_float//5,"张")
print("一角硬币：",money_float%5//1,"张")

# 格式化输出
num = 1024
print("输出{0}的十进制：{1:d}".format(num,num))
print("输出{0}的二进制：{1:b}".format(num,num))
print("输出{0}的八进制：{1:o}".format(num,num))
print("输出{0}的十六进制：{1:x}".format(num,num))
print("输出{0}的对应的Unicode字符：{1:c}".format(97,97))
num2=12345.12345
print("科学计数法表示：{:.2e}".format(num2))
print("浮点数位数(默认6位)：{:.2f}".format(num2))
print("输出浮点数百分形式：{:.2%}".format(num2))