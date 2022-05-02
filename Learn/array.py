array = ["a", "b", "c"];  # python列表==数组且可以用负数来倒数列表元素
print(array[2]);
array[0] = "text";
print(array[0]);
array.append("hefei");  # 列表最后添加元素
print(array[-1]);
print(array);
array.insert(2, "test");  # 在列表任意位置添加值
print(array);
del array[2];  # 删除列表索引值为2的值
print(array);
poptext = array.pop();  # 删除列表最后一位并将值赋予该函数，删除任意位置，括号内为索引值，没值则默认最后一位
print(poptext);
print(array);
array.remove("text");  # 删除列表对应的值
print(array);

# 对列表进行永久排序
array2 = ["c", "a", "d", "b", "e"];
array2.sort();  # 若字母小写则按字母顺序排序
print(array2);
array2.sort(reverse=True);  # 使用参数reverse来改变排序方式
print(array2);

# 列表临时排序
array3 = ["a", "e", "c", "d", "b"];
print("原始表：");
print(array3);
print("sorted方法临时排序：");
print(sorted(array3));
# 使用reverse方法反转列表
array3.reverse();  # 反转列表
print(array3);
# len函数获取列表长度
print(len(array3));
