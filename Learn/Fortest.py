array=["苹果","香蕉","菠萝","雪梨","草莓","西瓜"];
for arr in array:
    print(arr);
print("\n");
for arr2 in array:
    print("I like"+arr2);
print("水果真的很好吃");
#使用函数range生成一定范围的数字
for value in range(1,10):
    print(value);
numbers=list(range(1,10));#使用list将range转化为列表
print(numbers);
#range还可以指定定长
two_numbers=list(range(2,12,2));
print(two_numbers);

print(min(two_numbers));#最小值
print(max(two_numbers));#最大值
print(sum(two_numbers));#和

#平方数列表
num=[value**2 for value in range(1,11)]
print(num);
