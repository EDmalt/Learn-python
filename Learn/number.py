for value in range(1, 21):
    print(value)
num = list(range(1, 1000001))
print(num)
print("最小值：" + str(min(num)))
print("最大值：" + str(max(num)))
print("总和：" + str(sum(num)))

num1 = list(range(1, 21, 2))
print("1-20所有奇数：" + str(num1))

num3 = list(range(3, 31))
for value in num3:
    if value % 3 == 0:
        print(value)
