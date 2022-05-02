# By hefei
#1-100累加和
i=1
x=1
while i<100:
    i+=1
    x+=i
print("1-100的累加和={}".format(x))

#计算数字之和
num=eval(input("请输入一个数字:"))
temp=num
sum=0
while temp!=0:
    sum+=temp%10
    temp//=10
print("数字之和为",sum)

#计算某宝超过1万亿营业额需要多少年
num2=2600.0
year=0;
while num2<10000.0:
    num2*=1.25
    year+=1
    print("第{}年营业额为{}".format(year,num2))
print("第{}年营业额超过1万亿".format(year))