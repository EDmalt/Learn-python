string = "hello word.python!";
name = "hefei";
space = "abcbe    ";  # 设置一个带有空格的变量
print(string);
print(string.title());  # 设置单词首字母大写
print(string.upper());  # 设置单词全大写
print(string.lower());  # 设置字符全小写
print(string + " " + name.upper());  # 使用加号可链接两个变量
space = space.rstrip();  # 将该变量末尾的空格删除再赋予该变量=永久删除末尾空格
print(space);
