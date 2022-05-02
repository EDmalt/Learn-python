array = ["b北京", "g广东", "q青海", "s上海", "x西藏", "j江西"];
print(array);  # 原始顺序
print(sorted(array));  # 按字母临时排序
print(array);  # 重新打印查看是否改变
print(sorted(array, reverse=True));  # 按字母倒序临时排列
print(array);  # 验证是否改变原有顺序

array.reverse();  # 反转列表
print(array);  # 打印列表，验证是否反转
array.reverse();  # 再次反转列表
print(array);  # 打印查看列表是否反转回去

array.sort();  # 修改列表排序
print(array);  # 打印列表查看是否修改
array.sort(reverse=True);  # 修改列表排序：字母倒序
print(array);  # 打印查看是否修改

# for循环
print("for循环练习");
for arr in array:
    print(arr + "真漂亮");
